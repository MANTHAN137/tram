# Generated by Django 3.2.19 on 2023-07-17 19:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tram', '0010_auto_20211209_1708'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attackobject',
            name='attack_id',
            field=models.CharField(max_length=128),
        ),
        migrations.AlterField(
            model_name='attackobject',
            name='stix_id',
            field=models.CharField(max_length=128),
        ),
    ]
