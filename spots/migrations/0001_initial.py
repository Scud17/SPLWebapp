# Generated by Django 2.0.4 on 2018-04-29 01:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Spots',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('spot_Num', models.CharField(max_length=3)),
                ('is_taken', models.BooleanField()),
            ],
        ),
    ]
