# Generated by Django 3.2.3 on 2021-05-22 06:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('intern', '0005_auto_20210522_0634'),
    ]

    operations = [
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=1000)),
                ('country_id', models.IntegerField()),
            ],
        ),
    ]
