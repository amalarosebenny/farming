# Generated by Django 4.2.3 on 2023-07-23 18:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_person_address_alter_person_dob_alter_person_email_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='gender',
            field=models.CharField(choices=[('other', 'OTHER'), ('male', 'MALE'), ('female', 'FEMALE')], default='user', max_length=10),
        ),
    ]
