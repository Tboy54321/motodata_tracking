# Generated by Django 4.2.16 on 2024-12-16 20:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('users', '0003_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customerprofile',
            name='email',
        ),
        migrations.RemoveField(
            model_name='customerprofile',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='customerprofile',
            name='last_name',
        ),
        migrations.AlterField(
            model_name='customerprofile',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='customerprofile',
            name='phone_number',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='customerprofile',
            name='user',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='customerprofile', to=settings.AUTH_USER_MODEL),
        ),
    ]
