# Generated by Django 3.2.9 on 2022-01-11 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_rename_profile_item'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='childAge2',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='item',
            name='childAge3',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='item',
            name='childAge4',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='item',
            name='childAge5',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='item',
            name='hobby2',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='item',
            name='hobby3',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='item',
            name='language2',
            field=models.CharField(blank=True, choices=[('ENG', 'English'), ('SPA', 'Spanish'), ('FRA', 'French'), ('DEU', 'German'), ('POR', 'Portuguese')], default='ENG', max_length=3),
        ),
        migrations.AlterField(
            model_name='item',
            name='language3',
            field=models.CharField(blank=True, choices=[('ENG', 'English'), ('SPA', 'Spanish'), ('FRA', 'French'), ('DEU', 'German'), ('POR', 'Portuguese')], default='ENG', max_length=3),
        ),
    ]
