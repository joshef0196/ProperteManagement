# Generated by Django 2.0.3 on 2019-09-13 06:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0003_blog'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='Status',
            field=models.BooleanField(default=True),
        ),
    ]
