# Generated by Django 5.1.2 on 2025-01-25 06:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0009_tblproductcarts'),
    ]

    operations = [
        migrations.AddField(
            model_name='tblproductcarts',
            name='priceOut',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
