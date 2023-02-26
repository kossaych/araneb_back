# Generated by Django 4.1.6 on 2023-02-26 17:41

from django.db import migrations, models
import django.db.models.deletion
import pages.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cour',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre', models.CharField(blank=True, max_length=50, null=True)),
                ('intro', models.TextField(blank=True)),
                ('img', models.ImageField(blank=True, null=True, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Part',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre', models.CharField(blank=True, max_length=50, null=True)),
                ('content', models.TextField(blank=True)),
                ('img', models.ImageField(blank=True, null=True, upload_to=pages.models.upload_to)),
                ('code', models.TextField(blank=True)),
                ('cour', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='pages.cour')),
            ],
        ),
    ]