# Generated by Django 3.2.3 on 2021-05-22 06:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('intern', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('sortname', models.CharField(max_length=5)),
                ('name', models.CharField(max_length=1000)),
                ('phonecode', models.CharField(max_length=20)),
            ],
        ),
    ]
