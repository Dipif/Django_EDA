# Generated by Django 4.0.1 on 2022-01-07 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meatprice', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='meatsetting',
            name='year',
        ),
        migrations.AlterField(
            model_name='meatsetting',
            name='plot_type',
            field=models.CharField(default='Nothing', max_length=10, null=True),
        ),
    ]
