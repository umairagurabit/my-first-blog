# Generated by Django 2.2.12 on 2020-08-17 06:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_cv_list_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cv_list',
            name='title',
            field=models.CharField(max_length=200),
        ),
    ]