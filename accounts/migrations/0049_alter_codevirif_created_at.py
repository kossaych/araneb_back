# Generated by Django 4.1.1 on 2023-06-15 13:48

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0048_alter_codevirif_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='codevirif',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2023, 6, 15, 13, 48, 16, 875561, tzinfo=datetime.timezone.utc)),
        ),
    ]