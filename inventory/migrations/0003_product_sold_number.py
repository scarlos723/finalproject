# Generated by Django 3.1.3 on 2020-12-10 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0002_client_order_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='sold_number',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
