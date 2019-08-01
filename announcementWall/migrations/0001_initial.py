# Generated by Django 2.2.3 on 2019-08-01 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='WallPost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('wallpost_title', models.CharField(max_length=1000)),
                ('wallpost_text', models.TextField(max_length=5000)),
                ('pub_date', models.DateTimeField(verbose_name='Date Posted')),
            ],
        ),
    ]
