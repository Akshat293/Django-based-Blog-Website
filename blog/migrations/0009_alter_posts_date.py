# Generated by Django 4.1.3 on 2023-01-07 12:58

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_alter_posts_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='date',
            field=models.DateField(default=datetime.datetime(2023, 1, 7, 12, 58, 3, 667682, tzinfo=datetime.timezone.utc)),
        ),
    ]
