# Generated by Django 5.0.6 on 2024-07-05 07:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_supplier'),
    ]

    operations = [
        migrations.RenameField(
            model_name='supplier',
            old_name='mobileno',
            new_name='mobilno',
        ),
    ]