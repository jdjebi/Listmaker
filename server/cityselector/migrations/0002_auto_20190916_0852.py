# Generated by Django 2.2.1 on 2019-09-16 08:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cityselector', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='csvfile',
            options={'ordering': ('-date_creation',), 'verbose_name': 'Fichiers CSV', 'verbose_name_plural': 'Fichiers CSV'},
        ),
        migrations.AddField(
            model_name='csvfile',
            name='is_ok',
            field=models.BooleanField(default=False, verbose_name='etat du fichier de données'),
        ),
        migrations.AlterField(
            model_name='csvfile',
            name='path',
            field=models.CharField(default='nopath', max_length=255, verbose_name='chemin'),
        ),
    ]
