# Generated by Django 3.2.6 on 2021-08-30 08:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LibraryCounterSystemApp', '0002_auto_20210825_1648'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='isActive',
            field=models.BooleanField(default=True),
        ),
    ]
