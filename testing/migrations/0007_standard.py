# Generated by Django 2.1.3 on 2018-12-08 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testing', '0006_testing_test_time'),
    ]

    operations = [
        migrations.CreateModel(
            name='Standard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('perfectly', models.IntegerField(verbose_name='отлично')),
                ('good', models.IntegerField(verbose_name='хорошо')),
                ('passably', models.IntegerField(verbose_name='удовлетворительно')),
            ],
        ),
    ]