# Generated by Django 2.2 on 2019-04-24 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0016_auto_20181209_0810'),
    ]

    operations = [
        migrations.AddField(
            model_name='members',
            name='photo',
            field=models.ImageField(default=1, upload_to='avatar'),
            preserve_default=False,
        ),
    ]
