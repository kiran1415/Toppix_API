# Generated by Django 3.2.4 on 2021-06-22 18:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('toppix', '0002_auto_20210622_1829'),
    ]

    operations = [
        migrations.RenameField(
            model_name='toppix',
            old_name='Tags',
            new_name='tag',
        ),
    ]