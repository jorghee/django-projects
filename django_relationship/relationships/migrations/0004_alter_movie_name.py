# Generated by Django 5.0.6 on 2024-06-14 20:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('relationships', '0003_alter_character_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]
