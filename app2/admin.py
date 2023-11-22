from django.contrib import admin
from django.contrib.admin import ModelAdmin
from .models import UserProfile, VisitToTT, TextSlide, ImageSlide


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'workplace')

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(user=request.user)

    def has_change_permission(self, request, obj=None):
        if not obj:  # Добавление новой записи
            return True
        # Редактирование существующей записи
        return obj.user == request.user or request.user.is_superuser

    def get_model_perms(self, request):
        """
        Получение разрешений для модели.
        """
        # Для суперпользователя отображаем все
        if request.user.is_superuser:
            return super().get_model_perms(request)

        # Для обычных пользователей скрываем
        return {}


@admin.register(VisitToTT)
class VisitToTTAdmin(ModelAdmin):
    list_display = [
        'user_profile',
        'visits',
        'retail',
        'sto',
        'retail_buy_SAKURA_and_have',
        'sto_buy_SAKURA_and_have',
        'sto_dont_buy_SAKURA_and_have',
        'retail_dont_buy_SAKURA_and_have',
        'month'
    ]

    def save_model(self, request, obj, form, change):
        if not obj.user_profile:
            obj.user_profile = UserProfile.objects.get(user=request.user)
        super().save_model(request, obj, form, change)

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(user_profile__user=request.user)

    def has_change_permission(self, request, obj=None):
        if not obj:  # Добавление новой записи
            return True
        # Редактирование существующей записи
        return obj.user_profile.user == request.user or request.user.is_superuser

    def has_delete_permission(self, request, obj=None):
        if not obj:  # Удаление новой записи
            return True
        # Удаление существующей записи
        return obj.user_profile.user == request.user or request.user.is_superuser


@admin.register(TextSlide)
class TextSlideAdmin(ModelAdmin):
    list_display = [
        'visit',
        'user_profile',
        'title',
        'text'
    ]

    def save_model(self, request, obj, form, change):
        if not obj.user_profile:
            obj.user_profile = UserProfile.objects.get(user=request.user)
        super().save_model(request, obj, form, change)

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(user_profile__user=request.user)

    def has_change_permission(self, request, obj=None):
        if not obj:  # Добавление новой записи
            return True
        # Редактирование существующей записи
        return obj.user_profile.user == request.user or request.user.is_superuser

    def has_delete_permission(self, request, obj=None):
        if not obj:  # Удаление новой записи
            return True
        # Удаление существующей записи
        return obj.user_profile.user == request.user or request.user.is_superuser


@admin.register(ImageSlide)
class ImageSlideAdmin(ModelAdmin):
    list_display = [
        'visit',
        'user_profile',
        'title'
    ]

    def save_model(self, request, obj, form, change):
        if not obj.user_profile:
            obj.user_profile = UserProfile.objects.get(user=request.user)
        super().save_model(request, obj, form, change)

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(user_profile__user=request.user)

    def has_change_permission(self, request, obj=None):
        if not obj:  # Добавление новой записи
            return True
        # Редактирование существующей записи
        return obj.user_profile.user == request.user or request.user.is_superuser

    def has_delete_permission(self, request, obj=None):
        if not obj:  # Удаление новой записи
            return True
        # Удаление существующей записи
        return obj.user_profile.user == request.user or request.user.is_superuser