# Generated by Django 3.2.3 on 2021-07-10 08:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reiview',
            name='content',
            field=models.TextField(verbose_name='内容'),
        ),
        migrations.AlterField(
            model_name='reiview',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='写真'),
        ),
        migrations.AlterField(
            model_name='reiview',
            name='useful_review_record',
            field=models.TextField(verbose_name='講評'),
        ),
    ]