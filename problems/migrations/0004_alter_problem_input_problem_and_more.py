# Generated by Django 5.2.1 on 2025-05-18 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('problems', '0003_problem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='problem',
            name='input_problem',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='problem',
            name='output_problem',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
