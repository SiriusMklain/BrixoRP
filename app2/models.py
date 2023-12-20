from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.contrib.auth import get_user


class UserProfile(models.Model):
    """Пользователь"""
    role_list = (
        ('admin', 'Admin'),
        ('rbm', 'РБМ'),
        ('rp', 'РП')
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    workplace = models.CharField(max_length=255, verbose_name="Область работы")
    photo = models.ImageField(upload_to='user_photo/', blank=True, null=True)
    role = models.CharField(verbose_name='Роль участника', max_length=250, choices=role_list)
    rbm = models.ForeignKey('self', on_delete=models.SET_NULL, blank=True, null=True, related_name='rps', verbose_name='Подчиненный РБМ')

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'




class VisitToTT(models.Model):
    """Посещение ТТ:"""
    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE, editable=False, null=True)
    visits = models.CharField(max_length=255, verbose_name='Визитов (ТТ)')
    retail = models.CharField(max_length=255, verbose_name='Розничных ТТ')
    sto = models.CharField(max_length=255, verbose_name='СТО')
    retail_buy_SAKURA_and_have = models.CharField(max_length=255, verbose_name='Закупают SAKURA и есть в наличии')
    sto_buy_SAKURA_and_have = models.CharField(max_length=255, verbose_name='Закупают SAKURA и есть в наличии')
    sto_dont_buy_SAKURA_and_have = models.CharField(max_length=255, verbose_name='СТО Не закупают SAKURA или только под заказ в %')
    retail_dont_buy_SAKURA_and_have = models.CharField(max_length=255, verbose_name='Розничные ТТ Не закупают SAKURA или только под заказ в %')
    month = models.DateField(auto_now=False, auto_now_add=False, verbose_name='За какой месяц? в формате (гггг-мм)')

    def save(self, *args, **kwargs):
        # Подставляем текущего пользователя в поле user_profile перед сохранением
        if not self.user_profile:
            # Если поле user_profile не заполнено
            user_profile, created = UserProfile.objects.get_or_create(user=self.user)
            self.user_profile = user_profile
        super(VisitToTT, self).save(*args, **kwargs)

    def __str__(self):
        return f'{self.user_profile} {self.month}'

    class Meta:
        verbose_name = 'Посещение ТТ:'
        verbose_name_plural = 'Посещение ТТ:'


class TextSlide(models.Model):
    """Текстовый Слайдер"""
    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE, editable=False, null=True)
    visit = models.ForeignKey(VisitToTT, on_delete=models.CASCADE, related_name='text_slides', verbose_name='Посещение ТТ:')
    title = models.CharField(max_length=255, verbose_name='Заголовок листа')
    text = models.TextField(verbose_name="Текстовое поле")
    text_image = models.ImageField(upload_to='text_image/', blank=True, null=True)

    def save(self, *args, **kwargs):
        # Подставляем текущего пользователя в поле user_profile перед сохранением
        if not self.user_profile:
            # Если поле user_profile не заполнено
            user_profile, created = UserProfile.objects.get_or_create(user=self.user)
            self.user_profile = user_profile
        super(TextSlide, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Текстовый Слайдер'
        verbose_name_plural = 'Текстовые Слайдеры'
