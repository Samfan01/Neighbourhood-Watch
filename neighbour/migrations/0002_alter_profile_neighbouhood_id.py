# Generated by Django 3.2 on 2021-04-12 23:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('neighbour', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='neighbouhood_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='profile', to='neighbour.neighbourhood'),
        ),
    ]
