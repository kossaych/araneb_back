# Generated by Django 4.1.6 on 2023-02-26 17:41

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0031_rename_race_race_race_alter_codevirif_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='codevirif',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2023, 2, 26, 17, 41, 16, 427105, tzinfo=datetime.timezone.utc)),
        ),
    ]