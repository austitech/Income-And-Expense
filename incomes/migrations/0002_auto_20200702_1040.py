# Generated by Django 3.0.7 on 2020-07-02 09:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('incomes', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='income',
            old_name='SOURCE',
            new_name='source',
        ),
    ]
