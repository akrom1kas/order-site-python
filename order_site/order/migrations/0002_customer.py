# Generated by Django 4.0.4 on 2022-04-12 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100, verbose_name='Name')),
                ('last_name', models.CharField(max_length=100, verbose_name='Surname')),
                ('email', models.EmailField(max_length=100, verbose_name='Email')),
            ],
            options={
                'ordering': ['last_name', 'first_name', 'email'],
            },
        ),
    ]
