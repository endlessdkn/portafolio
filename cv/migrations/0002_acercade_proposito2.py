# Generated by Django 4.1.4 on 2022-12-20 00:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cv', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='acercade',
            name='Proposito2',
            field=models.TextField(blank=True, help_text='Describa el proposito por el cual busca empleo', null=True, verbose_name='Proposito'),
        ),
    ]
