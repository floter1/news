# Generated by Django 2.2 on 2019-04-27 23:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0017_members_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='members',
            name='photo',
            field=models.ImageField(default='avatars/default/default.jpg', upload_to='avatar'),
        ),
    ]
