# Generated by Django 3.1.1 on 2020-10-25 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cours', '0005_auto_20201025_1748'),
    ]

    operations = [
        migrations.AlterField(
            model_name='niveau_scolaire',
            name='nom',
            field=models.CharField(choices=[('Prepremaire', 'pré primaire'), ('Premaire', 'primaire'), ('Moyen', 'moyen'), ('Lycee', 'lycée'), ('Universitaire', 'Université')], max_length=15, unique=True),
        ),
    ]
