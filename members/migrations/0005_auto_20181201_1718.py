# Generated by Django 2.1.3 on 2018-12-01 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0004_auto_20181128_1018'),
    ]

    operations = [
        migrations.AddField(
            model_name='members',
            name='money',
            field=models.CharField(default=1, max_length=250),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='members',
            name='point',
            field=models.CharField(default=1, max_length=250),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='members',
            name='tin',
            field=models.CharField(default=1, max_length=250),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='members',
            name='upline',
            field=models.CharField(default=1, max_length=250),
            preserve_default=False,
        ),
    ]
