# Generated by Django 3.2.3 on 2021-07-11 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0007_review_useful_review_record'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='useful_review_record',
            field=models.TextField(default='a'),
        ),
    ]