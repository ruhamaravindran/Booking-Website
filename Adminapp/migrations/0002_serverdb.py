# Generated by Django 3.2.15 on 2022-11-15 06:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Adminapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Serverdb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('branch', models.CharField(max_length=30)),
                ('price', models.IntegerField()),
                ('image', models.ImageField(default='null.jpg', upload_to='Image')),
            ],
        ),
    ]