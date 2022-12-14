# Generated by Django 4.0.5 on 2022-07-25 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='cases',
            fields=[
                ('case_name', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('case_logo_url', models.TextField()),
                ('case_cost', models.TextField()),
            ],
            options={
                'db_table': 'cases',
            },
        ),
        migrations.CreateModel(
            name='guns',
            fields=[
                ('name', models.TextField(primary_key=True, serialize=False)),
                ('collection', models.TextField()),
                ('type', models.TextField()),
                ('rarity', models.TextField()),
                ('cost', models.TextField()),
                ('gun_url', models.TextField()),
            ],
            options={
                'db_table': 'guns',
            },
        ),
    ]
