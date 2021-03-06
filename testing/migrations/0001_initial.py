# Generated by Django 2.1.3 on 2018-12-01 05:44

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Fillin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField()),
                ('content', models.CharField(blank=True, max_length=100, null=True)),
                ('answer', models.CharField(max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Option',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(default='пишите описание выбора', max_length=40)),
                ('content', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Score',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.IntegerField()),
                ('last_updated_time', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Stem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=40)),
                ('number', models.IntegerField(null=True)),
                ('is_choicequestion', models.BooleanField(default=True)),
                ('content', ckeditor_uploader.fields.RichTextUploadingField(blank=True)),
                ('answer', models.CharField(max_length=40, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60, unique=True)),
                ('quantityOfTask', models.IntegerField(default=0)),
                ('grades', models.IntegerField(blank=True, null=True)),
                ('ranking', models.IntegerField(blank=True, null=True)),
                ('isDeleted', models.BooleanField(default=False)),
                ('last_updated_time', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'student',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Testing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, unique=True)),
                ('comment', models.TextField(null=True)),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('last_updated_time', models.DateTimeField(auto_now=True)),
                ('is_deleted', models.BooleanField(default=False)),
            ],
        ),
        migrations.AddField(
            model_name='stem',
            name='testing',
            field=models.ForeignKey(on_delete=False, to='testing.Testing'),
        ),
        migrations.AddField(
            model_name='score',
            name='student',
            field=models.ForeignKey(on_delete=False, to='testing.Student'),
        ),
        migrations.AddField(
            model_name='score',
            name='test',
            field=models.ForeignKey(on_delete=False, to='testing.Testing'),
        ),
        migrations.AddField(
            model_name='option',
            name='stem',
            field=models.ForeignKey(on_delete=False, to='testing.Stem'),
        ),
        migrations.AddField(
            model_name='fillin',
            name='stem',
            field=models.ForeignKey(on_delete=False, to='testing.Stem'),
        ),
        migrations.AlterUniqueTogether(
            name='stem',
            unique_together={('number', 'testing')},
        ),
        migrations.AlterUniqueTogether(
            name='score',
            unique_together={('test', 'student')},
        ),
        migrations.AlterUniqueTogether(
            name='fillin',
            unique_together={('number', 'stem')},
        ),
    ]
