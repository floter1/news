# Generated by Django 2.1.3 on 2018-12-01 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0013_auto_20181201_2107'),
    ]

    operations = [
        migrations.AlterField(
            model_name='members',
            name='age',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]