# Generated by Django 4.2.7 on 2023-11-30 10:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appapi', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='nome',
            new_name='name',
        ),
    ]
