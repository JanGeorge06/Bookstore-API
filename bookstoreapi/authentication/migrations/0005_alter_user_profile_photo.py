# Generated by Django 5.0 on 2024-01-07 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0004_remove_user_address_user_bio_user_profile_photo_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='profile_photo',
            field=models.ImageField(null=True, upload_to='images/'),
        ),
    ]
