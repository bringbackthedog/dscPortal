# Generated by Django 2.2.3 on 2019-08-05 03:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DSCEvent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dscevent_title', models.CharField(max_length=500)),
                ('dscevent_date', models.DateTimeField(verbose_name='Event Date')),
            ],
        ),
    ]