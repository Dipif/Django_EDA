# Generated by Django 4.0.1 on 2022-01-07 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MeatSetting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plot_type', models.CharField(default='Nothing', max_length=10)),
                ('year', models.IntegerField(default=2000)),
            ],
        ),
    ]