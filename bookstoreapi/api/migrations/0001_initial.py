# Generated by Django 5.0 on 2024-01-08 11:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('author', models.CharField(max_length=20)),
                ('genre', models.CharField(max_length=20)),
                ('price', models.DecimalField(decimal_places=2, max_digits=4)),
                ('publish_year', models.IntegerField()),
            ],
        ),
    ]