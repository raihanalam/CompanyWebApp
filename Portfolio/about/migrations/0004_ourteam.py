# Generated by Django 3.1.6 on 2021-02-20 21:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0003_auto_20210219_0328'),
    ]

    operations = [
        migrations.CreateModel(
            name='ourTeam',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('designation', models.CharField(max_length=100)),
                ('github', models.CharField(max_length=200)),
                ('linkedin', models.CharField(max_length=200)),
                ('twitter', models.CharField(max_length=200)),
                ('facebook', models.CharField(max_length=200)),
            ],
        ),
    ]