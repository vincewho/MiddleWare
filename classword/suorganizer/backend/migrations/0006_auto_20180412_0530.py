# Generated by Django 2.0.3 on 2018-04-12 05:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0005_auto_20180404_0539'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='manufacturer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.Manufacturer'),
        ),
    ]
