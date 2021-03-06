# Generated by Django 3.2.9 on 2022-01-25 12:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('penpals', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='penpalprofile',
            name='age',
            field=models.IntegerField(help_text='Your age'),
        ),
        migrations.AlterField(
            model_name='penpalprofile',
            name='childAge1',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='penpalprofile',
            name='childAge2',
            field=models.IntegerField(blank=True, help_text="Second child's age (optional)", null=True),
        ),
        migrations.AlterField(
            model_name='penpalprofile',
            name='childAge3',
            field=models.IntegerField(blank=True, help_text="Third child's age (optional)", null=True),
        ),
        migrations.AlterField(
            model_name='penpalprofile',
            name='childAge4',
            field=models.IntegerField(blank=True, help_text="Fourth child's age (optional)", null=True),
        ),
        migrations.AlterField(
            model_name='penpalprofile',
            name='childAge5',
            field=models.IntegerField(blank=True, help_text="Fifth child's age (optional)", null=True),
        ),
        migrations.AlterField(
            model_name='penpalprofile',
            name='hobby1',
            field=models.CharField(help_text='A hobby', max_length=50),
        ),
        migrations.AlterField(
            model_name='penpalprofile',
            name='hobby2',
            field=models.CharField(blank=True, help_text='Second hobby (optional)', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='penpalprofile',
            name='hobby3',
            field=models.CharField(blank=True, help_text='Third hobby (optional)', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='penpalprofile',
            name='name',
            field=models.CharField(help_text='Your name', max_length=50),
        ),
        migrations.AlterField(
            model_name='penpalprofile',
            name='pronoun',
            field=models.CharField(help_text='Your preferred pronoun/s)', max_length=50),
        ),
        migrations.AlterField(
            model_name='penpalprofile',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='penpal', to=settings.AUTH_USER_MODEL),
        ),
    ]
