# Generated by Django 3.1.1 on 2020-10-12 10:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Commentaire',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('commentaire', models.TextField(default='', max_length=2000)),
                ('nbrEtoiles', models.IntegerField(default=1)),
                ('acceptable', models.BooleanField(default=False)),
                ('proprietaire', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='accounts.etudiant')),
            ],
        ),
    ]
