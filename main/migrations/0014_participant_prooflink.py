# Generated by Django 3.0 on 2020-06-07 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_remove_event_poster'),
    ]

    operations = [
        migrations.AddField(
            model_name='participant',
            name='proofLink',
            field=models.CharField(blank=True, max_length=10000),
        ),
    ]
