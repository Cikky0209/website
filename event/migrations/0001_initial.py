# Generated by Django 4.2.14 on 2024-09-18 03:37

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
            name='VisitorLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip_address', models.GenericIPAddressField(verbose_name='Visitor IP Address')),
                ('timestamp', models.DateTimeField(auto_now_add=True, verbose_name='Visit Time')),
                ('page_url', models.URLField(verbose_name='Visited Page')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Visitor User')),
            ],
            options={
                'verbose_name': 'Visitor Log',
                'verbose_name_plural': 'Visitor Logs',
                'ordering': ['-timestamp'],
            },
        ),
        migrations.CreateModel(
            name='UserClickEvent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('page_url', models.URLField(verbose_name='Page')),
                ('clicked_element', models.CharField(max_length=255, verbose_name='Clicked Element')),
                ('click_time', models.DateTimeField(auto_now_add=True, verbose_name='Click Time')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
            options={
                'verbose_name': 'User Click Event',
                'verbose_name_plural': 'User Click Events',
                'ordering': ['-click_time'],
            },
        ),
    ]
