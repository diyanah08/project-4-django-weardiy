# Generated by Django 2.2.4 on 2019-11-11 07:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_auto_20191111_0706'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='postal_code',
            field=models.CharField(max_length=12),
        ),
    ]
