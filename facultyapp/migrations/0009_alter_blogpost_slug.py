# Generated by Django 5.0.7 on 2024-10-09 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('facultyapp', '0008_alter_blogpost_options_remove_blogpost_pub_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='slug',
            field=models.SlugField(blank=True, unique=True),
        ),
    ]
