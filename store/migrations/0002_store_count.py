# Generated by Django 3.1.3 on 2022-12-18 04:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='store',
            name='count',
            field=models.IntegerField(default=100),
            preserve_default=False,
        ),
    ]