# Generated by Django 3.2.7 on 2021-09-25 21:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0004_alter_services_service_icon'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='contact_email',
            field=models.EmailField(default='', max_length=254),
        ),
    ]