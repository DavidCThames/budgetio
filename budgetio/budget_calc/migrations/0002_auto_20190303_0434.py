# Generated by Django 2.1.7 on 2019-03-03 04:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('budget_calc', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ExpencesLookupTable',
            new_name='Expenceses',
        ),
    ]