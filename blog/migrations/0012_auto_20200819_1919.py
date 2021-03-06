# Generated by Django 2.2.12 on 2020-08-19 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_auto_20200819_0122'),
    ]

    operations = [
        migrations.CreateModel(
            name='CV_list',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('researches', models.TextField()),
                ('education', models.TextField()),
                ('work_experience', models.TextField()),
                ('reference', models.TextField()),
                ('technical_skills', models.TextField()),
                ('published_date', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='CV_education',
        ),
        migrations.DeleteModel(
            name='CV_reference',
        ),
        migrations.DeleteModel(
            name='CV_research',
        ),
        migrations.DeleteModel(
            name='CV_technical_skills',
        ),
        migrations.DeleteModel(
            name='CV_work_experience',
        ),
    ]
