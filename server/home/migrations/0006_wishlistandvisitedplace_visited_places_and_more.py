# Generated by Django 4.0.3 on 2022-03-07 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_wishlistandvisitedplace_remove_wishlist_user_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='wishlistandvisitedplace',
            name='visited_places',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='wishlistandvisitedplace',
            name='wishlist',
            field=models.TextField(default=''),
        ),
    ]
