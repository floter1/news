# Generated by Django 2.1.3 on 2018-12-01 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0006_auto_20181201_1730'),
    ]

    operations = [
        migrations.AlterField(
            model_name='members',
            name='age',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='members',
            name='money',
            field=models.FloatField(max_length=250),
        ),
        migrations.AlterField(
            model_name='members',
            name='points',
            field=models.FloatField(max_length=250),
        ),
    ]
