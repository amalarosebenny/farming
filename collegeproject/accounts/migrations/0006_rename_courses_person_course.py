# Generated by Django 4.2.3 on 2023-07-24 08:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_alter_person_gender'),
    ]

    operations = [
        migrations.RenameField(
            model_name='person',
            old_name='courses',
            new_name='course',
        ),
    ]
