# Generated by Django 2.1.7 on 2019-03-18 02:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('imi_status', '0002_auto_20190317_2146'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='imistatus',
            options={'ordering': ['-timestamp']},
        ),
    ]
