# Generated by Django 3.1.1 on 2020-11-01 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('formation', '0008_auto_20201101_1327'),
    ]

    operations = [
        migrations.AlterField(
            model_name='formation',
            name='formation_type',
            field=models.CharField(choices=[('OR', 'Or'), ('NORMAL', 'Normal')], max_length=20, verbose_name='Type de formation'),
        ),
    ]