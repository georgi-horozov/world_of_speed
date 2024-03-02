# Generated by Django 4.2.10 on 2024-02-24 08:08

import django.core.validators
from django.db import migrations, models
import world_of_speed.profile_app.validators


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=15, validators=[world_of_speed.profile_app.validators.validator_username, world_of_speed.profile_app.validators.validate_username_length])),
                ('email', models.EmailField(max_length=254)),
                ('age', models.IntegerField(help_text='Age requirement: 21 years and above.', validators=[django.core.validators.MinValueValidator(21)])),
                ('password', models.CharField(max_length=20)),
                ('first_name', models.CharField(blank=True, max_length=25, null=True)),
                ('last_name', models.CharField(blank=True, max_length=25, null=True)),
                ('profile_picture', models.URLField(blank=True, null=True)),
            ],
        ),
    ]
