# Generated by Django 2.2.10 on 2020-08-20 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=15)),
                ('notes', models.TextField(max_length=200)),
                ('value', models.DecimalField(decimal_places=2, max_digits=3)),
                ('proof', models.ImageField(upload_to='')),
            ],
        ),
    ]
