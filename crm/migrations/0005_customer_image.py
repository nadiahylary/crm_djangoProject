# Generated by Django 4.2 on 2023-04-21 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0004_alter_customer_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='image',
            field=models.ImageField(null=True, upload_to='customer-profiles'),
        ),
    ]
