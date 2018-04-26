# Generated by Django 2.0.3 on 2018-04-19 19:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='manufacturer',
            name='address',
            field=models.TextField(default='Some Place Ave.'),
        ),
        migrations.AddField(
            model_name='testlab',
            name='country',
            field=models.CharField(default='USA', max_length=100),
        ),
        migrations.AlterField(
            model_name='testlab',
            name='address',
            field=models.TextField(default='Some Place Ave.'),
        ),
    ]
