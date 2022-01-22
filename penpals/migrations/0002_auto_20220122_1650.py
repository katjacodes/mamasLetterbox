# Generated by Django 3.2.9 on 2022-01-22 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('penpals', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='penpalprofile',
            name='user',
        ),
        migrations.AddField(
            model_name='penpalprofile',
            name='email',
            field=models.EmailField(default='Please complete', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='penpalprofile',
            name='language1',
            field=models.CharField(choices=[('ENG', 'English'), ('SPA', 'Spanish'), ('FRA', 'French'), ('DEU', 'German'), ('POR', 'Portuguese')], default='ENG', max_length=3),
        ),
        migrations.AddField(
            model_name='penpalprofile',
            name='language2',
            field=models.CharField(blank=True, choices=[('ENG', 'English'), ('SPA', 'Spanish'), ('FRA', 'French'), ('DEU', 'German'), ('POR', 'Portuguese')], default='ENG', max_length=3, null=True),
        ),
        migrations.AddField(
            model_name='penpalprofile',
            name='language3',
            field=models.CharField(blank=True, choices=[('ENG', 'English'), ('SPA', 'Spanish'), ('FRA', 'French'), ('DEU', 'German'), ('POR', 'Portuguese')], default='ENG', max_length=3, null=True),
        ),
        migrations.AddField(
            model_name='penpalprofile',
            name='name',
            field=models.CharField(default='exit', max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='penpalprofile',
            name='childAge1',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='penpalprofile',
            name='childAge2',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='penpalprofile',
            name='childAge3',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='penpalprofile',
            name='childAge4',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='penpalprofile',
            name='childAge5',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='penpalprofile',
            name='hobby1',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='penpalprofile',
            name='hobby2',
            field=models.CharField(blank=True, default='Second Hobby', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='penpalprofile',
            name='hobby3',
            field=models.CharField(blank=True, default='Third Hobby', max_length=50, null=True),
        ),
    ]
