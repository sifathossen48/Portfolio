# Generated by Django 4.2 on 2023-07-12 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0003_alter_info_dribble_alter_info_facebook_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('desc', models.TextField(blank=True, null=True)),
                ('resume_title', models.CharField(max_length=150)),
                ('contact_title', models.CharField(max_length=150)),
                ('contact_desc', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
