# Generated by Django 3.2.6 on 2022-02-28 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lists', '0003_alter_tasks_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tasks',
            name='slug',
            field=models.SlugField(default='none', unique=True),
        ),
    ]
