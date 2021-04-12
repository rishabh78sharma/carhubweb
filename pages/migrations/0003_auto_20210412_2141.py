# Generated by Django 3.0.7 on 2021-04-12 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_auto_20210412_1551'),
    ]

    operations = [
        migrations.RenameField(
            model_name='team',
            old_name='instagram_link',
            new_name='google_link',
        ),
        migrations.AlterField(
            model_name='team',
            name='photo',
            field=models.ImageField(upload_to='photo/%y/%m/%d/'),
        ),
    ]
