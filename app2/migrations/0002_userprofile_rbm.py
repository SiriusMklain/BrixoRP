# Generated by Django 4.2.6 on 2023-12-14 08:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app2', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='rbm',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='rps', to='app2.userprofile', verbose_name='Подчиненный РБМ'),
        ),
    ]
