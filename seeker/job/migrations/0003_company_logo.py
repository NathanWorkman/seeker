# Generated by Django 2.2.9 on 2020-01-15 01:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0002_tag'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='logo',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
