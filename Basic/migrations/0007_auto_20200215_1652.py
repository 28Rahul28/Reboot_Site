# Generated by Django 3.0.3 on 2020-02-15 11:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Basic', '0006_auto_20200215_1531'),
    ]

    operations = [
        migrations.RenameField(
            model_name='events',
            old_name='features',
            new_name='keywords',
        ),
    ]
