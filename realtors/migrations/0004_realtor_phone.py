# Generated by Django 2.1.3 on 2018-11-18 04:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('realtors', '0003_auto_20181118_0421'),
    ]

    operations = [
        migrations.AddField(
            model_name='realtor',
            name='phone',
            field=models.CharField(default='****', max_length=20),
        ),
    ]
