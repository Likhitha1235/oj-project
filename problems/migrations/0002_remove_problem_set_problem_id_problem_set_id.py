# Generated by Django 5.2.1 on 2025-05-18 02:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('problems', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='problem_set',
            name='problem_id',
        ),
        migrations.AddField(
            model_name='problem_set',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
