# Generated by Django 4.0.4 on 2022-06-03 11:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_quality_inspection'),
    ]

    operations = [
        migrations.RenameField(
            model_name='quality_inspection',
            old_name='date_t',
            new_name='date',
        ),
    ]
