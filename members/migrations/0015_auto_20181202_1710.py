# Generated by Django 2.1.3 on 2018-12-02 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0014_auto_20181201_2301'),
    ]

    operations = [
        migrations.AlterField(
            model_name='members',
            name='money',
            field=models.FloatField(blank=True, default=0.0, null=True),
        ),
        migrations.AlterField(
            model_name='members',
            name='points',
            field=models.FloatField(blank=True, default=0.0, null=True),
        ),
    ]
