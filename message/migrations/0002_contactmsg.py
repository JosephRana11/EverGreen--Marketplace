# Generated by Django 4.2.4 on 2023-09-30 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('message', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactMsg',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('contact', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('msg', models.TextField()),
            ],
        ),
    ]
