# Generated by Django 4.2 on 2023-07-11 20:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='info',
            name='dribble',
            field=models.URLField(default=1, max_length=30),
            preserve_default=False,
        ),
    ]
