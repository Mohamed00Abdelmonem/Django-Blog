# Generated by Django 4.2 on 2023-07-27 19:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='draft2',
            field=models.BooleanField(default=True),
        ),
    ]
