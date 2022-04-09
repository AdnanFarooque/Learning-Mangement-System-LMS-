# Generated by Django 2.2.1 on 2019-09-05 06:31

import classroom.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choice', models.CharField(max_length=200)),
                ('isAnswer', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Discussion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('discussion', models.TextField()),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
            ],
        ),
        migrations.CreateModel(
            name='DiscussionId',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('discussionId', models.IntegerField(default=classroom.models.DiscussionId.make_discussionId, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Marks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mark', models.CharField(default='A', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Quiz',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
                ('last_date', models.DateTimeField(verbose_name='last date')),
                ('time', models.TimeField(verbose_name='exam time')),
            ],
        ),
        migrations.CreateModel(
            name='Resource',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('resource', models.FileField(blank=True, null=True, upload_to='resources')),
                ('pub_date', models.DateTimeField(verbose_name='data published')),
            ],
        ),
        migrations.CreateModel(
            name='TermDate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dateStart', models.DateTimeField(verbose_name='Term started')),
                ('dateEnd', models.DateTimeField(verbose_name='Term ended')),
            ],
        ),
    ]