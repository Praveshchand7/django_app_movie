# Generated by Django 5.0.6 on 2024-07-07 20:29

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2024, 7, 7, 20, 29, 15, 621137, tzinfo=datetime.timezone.utc)),
        ),
    ]
