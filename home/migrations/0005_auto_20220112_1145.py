# Generated by Django 3.2.9 on 2022-01-12 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_auto_20220111_1742'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='childAge2',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='item',
            name='childAge3',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='item',
            name='childAge4',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='item',
            name='childAge5',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='item',
            name='hobby2',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='item',
            name='hobby3',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]