# Generated by Django 2.1.5 on 2019-02-14 07:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('HealthCentre', '0008_prescription_new'),
    ]

    operations = [
        migrations.RenameField(
            model_name='prescription',
            old_name='new',
            new_name='isNew',
        ),
    ]