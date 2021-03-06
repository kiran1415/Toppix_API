# Generated by Django 3.2.4 on 2021-06-22 18:29

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('toppix', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tags',
            options={'verbose_name': 'Tag'},
        ),
        migrations.AddField(
            model_name='toppix',
            name='created_on',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='toppix',
            name='updated_on',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
