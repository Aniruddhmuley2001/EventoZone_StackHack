# Generated by Django 3.0 on 2020-06-04 07:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20200604_1239'),
    ]

    operations = [
        migrations.AddField(
            model_name='participant',
            name='EventID',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
