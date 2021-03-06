# Generated by Django 3.1 on 2021-05-05 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EcomApp', '0005_faq'),
    ]

    operations = [
        migrations.DeleteModel(
            name='FAQ',
        ),
        migrations.RemoveField(
            model_name='contactmessage',
            name='Note',
        ),
        migrations.RemoveField(
            model_name='contactmessage',
            name='ip',
        ),
        migrations.RemoveField(
            model_name='setting',
            name='contact',
        ),
        migrations.RemoveField(
            model_name='setting',
            name='fax',
        ),
        migrations.RemoveField(
            model_name='setting',
            name='reference',
        ),
        migrations.RemoveField(
            model_name='setting',
            name='smptpassword',
        ),
        migrations.RemoveField(
            model_name='setting',
            name='smptport',
        ),
        migrations.RemoveField(
            model_name='setting',
            name='smptserver',
        ),
        migrations.RemoveField(
            model_name='setting',
            name='smtpemail',
        ),
        migrations.AlterField(
            model_name='setting',
            name='address',
            field=models.CharField(max_length=200),
        ),
    ]
