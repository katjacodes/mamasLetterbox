# Generated by Django 3.2.9 on 2022-01-27 20:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('penpals', '0004_auto_20220127_2004'),
    ]

    operations = [
        migrations.AlterField(
            model_name='penpalprofile',
            name='childAge1',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='penpalprofile',
            name='childAge2',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='penpalprofile',
            name='childAge3',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='penpalprofile',
            name='childAge4',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='penpalprofile',
            name='childAge5',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='penpalprofile',
            name='hobby1',
            field=models.CharField(default='Something you enjoy', max_length=50),
        ),
        migrations.AlterField(
            model_name='penpalprofile',
            name='hobby2',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='penpalprofile',
            name='hobby3',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='penpalprofile',
            name='pronoun',
            field=models.CharField(default='Your preferred pronoun/s)', max_length=50),
        ),
    ]
