# Generated by Django 3.0.7 on 2021-04-12 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='team',
            old_name='created_daten',
            new_name='created_date',
        ),
        migrations.AddField(
            model_name='team',
            name='designation',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='team',
            name='instagram_link',
            field=models.URLField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='team',
            name='last_name',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='team',
            name='twitter_link',
            field=models.URLField(default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='team',
            name='facebook_link',
            field=models.URLField(default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='team',
            name='first_name',
            field=models.CharField(default='', max_length=255),
        ),
    ]
