# Generated by Django 3.1.1 on 2020-10-31 16:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('formation', '0006_auto_20201029_1113'),
    ]

    operations = [
        migrations.AlterField(
            model_name='formation',
            name='categorie',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='formation.categorie', verbose_name='Catégorie'),
        ),
        migrations.AlterField(
            model_name='formation',
            name='formation_type',
            field=models.CharField(choices=[('OR', 'Or'), ('NORMAL', 'Normal')], max_length=20, verbose_name='Type de formation'),
        ),
    ]
