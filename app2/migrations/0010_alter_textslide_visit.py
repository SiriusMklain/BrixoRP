# Generated by Django 4.2.6 on 2023-11-22 16:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app2', '0009_imageslide_user_profile_textslide_user_profile_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='textslide',
            name='visit',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='text_slides', to='app2.visittott'),
        ),
    ]