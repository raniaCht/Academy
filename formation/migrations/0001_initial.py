# Generated by Django 3.1.1 on 2020-09-27 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categorie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=50)),
                ('nom_en', models.CharField(max_length=50, null=True)),
                ('nom_fr', models.CharField(max_length=50, null=True)),
                ('nom_ar', models.CharField(max_length=50, null=True)),
            ],
        ),
    ]
