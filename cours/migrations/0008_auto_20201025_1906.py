# Generated by Django 3.1.1 on 2020-10-25 18:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cours', '0007_auto_20201025_1903'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cours',
            name='annee',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cours.annee', verbose_name='Année'),
        ),
    ]