# Generated by Django 3.2.9 on 2022-07-18 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='touruser',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='touruser',
            name='is_staff',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='touruser',
            name='phone_number',
            field=models.CharField(blank=True, max_length=12, null=True, unique=True),
        ),
    ]
