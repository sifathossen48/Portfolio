# Generated by Django 4.2 on 2023-07-17 18:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0010_education'),
    ]

    operations = [
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('percentage', models.CharField(max_length=5)),
            ],
        ),
    ]