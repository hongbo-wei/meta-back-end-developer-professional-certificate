# Generated by Django 5.0.1 on 2024-03-11 18:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('LittleLemonAPI', '0003_delete_userprofile'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cart',
            options={'ordering': ['id']},
        ),
    ]
