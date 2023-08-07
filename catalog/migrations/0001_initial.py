# Generated by Django 4.2.4 on 2023-08-07 07:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=255)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('deadline', models.DateTimeField()),
                ('completed', models.BooleanField()),
                ('tags', models.ManyToManyField(related_name='tasks', to='catalog.tag')),
            ],
            options={
                'ordering': ['completed', '-created'],
            },
        ),
    ]
