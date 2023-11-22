# Generated by Django 4.2.6 on 2023-11-22 13:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('workplace', models.CharField(max_length=255)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='VisitToTT',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('visits', models.CharField(max_length=255, verbose_name='Визитов (ТТ)')),
                ('retail', models.CharField(max_length=255, verbose_name='Розничных ТТ')),
                ('sto', models.CharField(max_length=255, verbose_name='СТО')),
                ('retail_buy_SAKURA_and_have', models.CharField(max_length=255, verbose_name='Закупают SAKURA и есть в наличии')),
                ('sto_buy_SAKURA_and_have', models.CharField(max_length=255, verbose_name='Закупают SAKURA и есть в наличии')),
                ('sto_dont_buy_SAKURA_and_have', models.CharField(max_length=255, verbose_name='СТО Не закупают SAKURA или только под заказ в %')),
                ('retail_dont_buy_SAKURA_and_have', models.CharField(max_length=255, verbose_name='Розничные ТТ Не закупают SAKURA или только под заказ в %')),
                ('month', models.DateField(verbose_name='За какой месяц?')),
                ('user_profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app2.userprofile')),
            ],
        ),
        migrations.CreateModel(
            name='TextSlide',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Заголовок листа')),
                ('text', models.TextField(verbose_name='Текстовое поле')),
                ('visit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app2.visittott')),
            ],
        ),
        migrations.CreateModel(
            name='ImageSlide',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Заголовок листа')),
                ('image', models.ImageField(upload_to='image_slide/')),
                ('visit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app2.visittott')),
            ],
        ),
    ]