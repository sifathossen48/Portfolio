# Generated by Django 4.2 on 2023-07-17 18:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0009_experience'),
    ]

    operations = [
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=40)),
                ('degree', models.CharField(max_length=40)),
                ('timeline', models.CharField(max_length=30)),
                ('desc', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
