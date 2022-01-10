# Generated by Django 3.2.9 on 2021-12-27 18:48

from django.db import migrations, models
import django_countries.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language1', models.CharField(choices=[('ENG', 'English'), ('SPA', 'Spanish'), ('FRA', 'French'), ('DEU', 'German'), ('POR', 'Portuguese')], default='ENG', max_length=3)),
                ('language2', models.CharField(choices=[('ENG', 'English'), ('SPA', 'Spanish'), ('FRA', 'French'), ('DEU', 'German'), ('POR', 'Portuguese')], default='ENG', max_length=3)),
                ('language3', models.CharField(choices=[('ENG', 'English'), ('SPA', 'Spanish'), ('FRA', 'French'), ('DEU', 'German'), ('POR', 'Portuguese')], default='ENG', max_length=3)),
                ('name', models.CharField(max_length=50)),
                ('pronoun', models.CharField(max_length=50)),
                ('age', models.IntegerField()),
                ('country', django_countries.fields.CountryField(max_length=2)),
                ('hobby1', models.CharField(max_length=50)),
                ('hobby2', models.CharField(max_length=50)),
                ('hobby3', models.CharField(max_length=50)),
                ('childAge1', models.IntegerField()),
                ('childAge2', models.IntegerField()),
                ('childAge3', models.IntegerField()),
                ('childAge4', models.IntegerField()),
                ('childAge5', models.IntegerField()),
                ('email', models.EmailField(max_length=50)),
            ],
        ),
    ]
