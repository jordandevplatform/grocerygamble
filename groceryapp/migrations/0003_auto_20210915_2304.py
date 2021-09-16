# Generated by Django 2.2 on 2021-09-15 23:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('groceryapp', '0002_breakfastgenre_breakfastingredient_dinnergenre_dinneringredient_lunchgenre_lunchingredient'),
    ]

    operations = [
        migrations.AddField(
            model_name='breakfastgenre',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='breakfastgenre',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='bgenres', to='groceryapp.User'),
        ),
        migrations.AddField(
            model_name='breakfastingredient',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='breakfastingredient',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='bingredients', to='groceryapp.User'),
        ),
        migrations.AddField(
            model_name='dinnergenre',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='dinneringredient',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='lunchgenre',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='lunchingredient',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
