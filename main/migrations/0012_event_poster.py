# Generated by Django 3.0 on 2020-06-06 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_remove_event_poster'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='Poster',
            field=models.ImageField(blank=True, null=True, upload_to='posters'),
        ),
    ]
