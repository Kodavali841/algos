# Generated by Django 3.0.3 on 2021-05-20 07:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='subject',
            old_name='body',
            new_name='name',
        ),
    ]
