# Generated by Django 4.2 on 2023-07-17 19:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0011_skill'),
    ]

    operations = [
        migrations.CreateModel(
            name='Testimonial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author_name', models.CharField(max_length=30)),
                ('author_title', models.CharField(max_length=30)),
                ('author_image', models.ImageField(upload_to='testimonial/')),
                ('desc', models.TextField(blank=True, null=True)),
            ],
        ),
    ]