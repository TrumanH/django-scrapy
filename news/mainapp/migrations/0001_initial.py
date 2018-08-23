# Generated by Django 2.1 on 2018-08-22 02:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='dailyNews',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('datetime', models.DateTimeField()),
                ('value', models.CharField(max_length=30)),
                ('forecast', models.CharField(max_length=30)),
                ('previous', models.CharField(max_length=30)),
                ('star', models.IntegerField()),
            ],
            options={
                'db_table': 'dailynews',
                'ordering': ['datetime'],
            },
        ),
    ]
