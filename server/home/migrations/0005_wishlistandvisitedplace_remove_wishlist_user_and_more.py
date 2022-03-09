# Generated by Django 4.0.3 on 2022-03-07 09:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('home', '0004_wishlist_visitedplace'),
    ]

    operations = [
        migrations.CreateModel(
            name='WishlistAndVisitedPlace',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('added_date', models.DateField()),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Wishlist and Visited Place',
                'verbose_name_plural': 'Wishlist andd Visited Places',
            },
        ),
        migrations.RemoveField(
            model_name='wishlist',
            name='user',
        ),
        migrations.DeleteModel(
            name='VisitedPlace',
        ),
        migrations.DeleteModel(
            name='Wishlist',
        ),
    ]