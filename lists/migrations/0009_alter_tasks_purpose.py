# Generated by Django 3.2.6 on 2022-02-28 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lists', '0008_alter_tasks_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tasks',
            name='purpose',
            field=models.CharField(choices=[('Personal', 'Personal'), ('Fitness', 'Fitness'), ('School', 'School'), ('Business', 'Business'), ('Office', 'Office')], default='Personal', max_length=8),
        ),
    ]
