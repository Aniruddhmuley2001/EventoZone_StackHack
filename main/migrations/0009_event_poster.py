# Generated by Django 3.0 on 2020-06-06 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_auto_20200604_1530'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='Poster',
            field=models.ImageField(default=0, upload_to=''),
            preserve_default=False,
        ),
    ]
