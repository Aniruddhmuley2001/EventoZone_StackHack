# Generated by Django 3.0 on 2020-06-04 08:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_participant_eventid'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='status',
            field=models.IntegerField(default=1),
        ),
    ]
