# Generated by Django 3.2.18 on 2023-03-21 08:32

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0033_alter_codevirif_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='codevirif',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2023, 3, 21, 8, 32, 0, 699403, tzinfo=utc)),
        ),
    ]
