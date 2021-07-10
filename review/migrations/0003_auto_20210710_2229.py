# Generated by Django 3.2.3 on 2021-07-10 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0002_auto_20210710_1730'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reiview',
            old_name='image',
            new_name='photo',
        ),
        migrations.RenameField(
            model_name='reiview',
            old_name='author',
            new_name='user',
        ),
        migrations.AlterField(
            model_name='reiview',
            name='evaluation',
            field=models.CharField(choices=[('良い', '良い'), ('悪い', '悪い')], max_length=10, verbose_name='評価'),
        ),
    ]
