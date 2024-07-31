# Generated by Django 5.0.7 on 2024-07-31 15:23

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0002_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='bouquet_makers_attendees',
            field=models.ManyToManyField(blank=True, related_name='bouquet_makers_attendees', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='event',
            name='drivers_attendees',
            field=models.ManyToManyField(blank=True, related_name='drivers_attendees', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='event',
            name='group',
            field=models.IntegerField(choices=[(1, 'Group 1'), (2, 'Group 2')]),
        ),
    ]