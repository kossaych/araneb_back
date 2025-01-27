# Generated by Django 4.1.1 on 2023-06-23 08:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0007_femalle_partenaire_lapinproduction_partenaire_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='femalle',
            name='partenaire',
        ),
        migrations.RemoveField(
            model_name='lapinproduction',
            name='partenaire',
        ),
        migrations.RemoveField(
            model_name='malle',
            name='partenaire',
        ),
        migrations.AddField(
            model_name='femalle',
            name='acouplements',
            field=models.ManyToManyField(through='manager.Accouplement', to='manager.malle'),
        ),
        migrations.AddField(
            model_name='malle',
            name='acouplements',
            field=models.ManyToManyField(through='manager.Accouplement', to='manager.femalle'),
        ),
    ]
