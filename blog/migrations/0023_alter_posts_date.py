# Generated by Django 4.1.3 on 2023-01-08 14:12

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0022_alter_posts_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='date',
            field=models.DateField(default=datetime.datetime(2023, 1, 8, 14, 12, 1, 994324, tzinfo=datetime.timezone.utc)),
        ),
    ]
