# Generated by Django 3.2.9 on 2021-12-15 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0024_auto_20211215_1348'),
    ]

    operations = [
        migrations.AlterField(
            model_name='readupdate',
            name='attachment_links',
            field=models.CharField(max_length=1500, null=True),
        ),
        migrations.AlterField(
            model_name='readupdate',
            name='image_links',
            field=models.CharField(max_length=3000, null=True),
        ),
        migrations.AlterField(
            model_name='readupdate',
            name='sku',
            field=models.CharField(max_length=750, null=True, unique=True),
        ),
    ]