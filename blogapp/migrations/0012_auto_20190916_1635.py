# Generated by Django 2.0.3 on 2019-09-16 10:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0011_auto_20190916_1520'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='seocontent',
            name='base_description',
        ),
        migrations.RemoveField(
            model_name='seocontent',
            name='base_detail_description',
        ),
        migrations.RemoveField(
            model_name='seocontent',
            name='base_detail_keywords',
        ),
        migrations.RemoveField(
            model_name='seocontent',
            name='base_keywords',
        ),
        migrations.RemoveField(
            model_name='seocontent',
            name='base_title',
        ),
        migrations.RemoveField(
            model_name='seocontent',
            name='blog_detail_title',
        ),
        migrations.RemoveField(
            model_name='seocontent',
            name='properties_detail_description',
        ),
        migrations.RemoveField(
            model_name='seocontent',
            name='properties_detail_keywords',
        ),
        migrations.RemoveField(
            model_name='seocontent',
            name='properties_detail_title',
        ),
    ]
