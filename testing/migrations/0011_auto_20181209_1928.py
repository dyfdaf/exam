# Generated by Django 2.1.3 on 2018-12-09 19:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testing', '0010_auto_20181209_1927'),
    ]

    operations = [
        migrations.AlterField(
            model_name='score',
            name='answer',
            field=models.TextField(blank=True, null=True, verbose_name='ответ студента   '),
        ),
    ]
