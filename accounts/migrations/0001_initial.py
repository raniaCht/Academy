# Generated by Django 3.1.1 on 2020-09-28 10:54

import accounts.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Etudiant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dateDeNais', models.DateField()),
                ('genre', models.CharField(choices=[('HOMME', 'Male'), ('FEMME', 'female')], max_length=10)),
                ('image', models.ImageField(default='default.png', upload_to=accounts.models.image_upload)),
                ('compte', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
