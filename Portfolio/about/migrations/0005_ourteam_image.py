# Generated by Django 3.1.6 on 2021-02-20 21:19

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0004_ourteam'),
    ]

    operations = [
        migrations.AddField(
            model_name='ourteam',
            name='image',
            field=models.ImageField(default=django.utils.timezone.now, upload_to='about/OurTeam'),
            preserve_default=False,
        ),
    ]
