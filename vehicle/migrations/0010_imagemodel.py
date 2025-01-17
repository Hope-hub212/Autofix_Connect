# Generated by Django 3.0.5 on 2024-12-06 20:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehicle', '0009_attendance'),
    ]

    operations = [
        migrations.CreateModel(
            name='ImageModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images/')),
                ('title', models.CharField(max_length=50)),
                ('price', models.CharField(max_length=50)),
            ],
        ),
    ]
