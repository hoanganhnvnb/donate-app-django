# Generated by Django 2.2 on 2021-10-16 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('donation', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donation',
            name='upvotes',
            field=models.IntegerField(default=0),
        ),
    ]
