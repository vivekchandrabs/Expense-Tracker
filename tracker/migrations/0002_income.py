# Generated by Django 3.0.3 on 2020-02-18 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Income',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('amount', models.IntegerField()),
                ('timestamp', models.DateTimeField()),
            ],
        ),
    ]
