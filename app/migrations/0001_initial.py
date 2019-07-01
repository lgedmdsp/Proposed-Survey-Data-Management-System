# Generated by Django 2.1.5 on 2019-02-24 06:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='data',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uniqueid', models.CharField(blank=True, max_length=200)),
                ('eduid', models.CharField(blank=True, max_length=200)),
                ('district', models.CharField(blank=True, max_length=200)),
                ('upazilla', models.CharField(blank=True, max_length=200)),
                ('s_union', models.CharField(blank=True, max_length=200)),
                ('mouza', models.CharField(blank=True, max_length=200)),
                ('village', models.CharField(blank=True, max_length=200)),
                ('sheltername', models.CharField(blank=True, max_length=200)),
                ('northing', models.FloatField(blank=True, null=True)),
                ('easting', models.FloatField(blank=True, null=True)),
                ('distance', models.FloatField(blank=True, null=True)),
                ('expectedpopulation', models.FloatField(blank=True, null=True)),
                ('waterlevel', models.FloatField(blank=True, null=True)),
                ('pucca', models.FloatField(blank=True, null=True)),
                ('semipucca', models.FloatField(blank=True, null=True)),
                ('wooden', models.FloatField(blank=True, null=True)),
                ('bamboo', models.FloatField(blank=True, null=True)),
                ('thatched', models.FloatField(blank=True, null=True)),
                ('shanty', models.FloatField(blank=True, null=True)),
                ('total_house', models.FloatField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='District',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Upazilla',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.District')),
            ],
        ),
    ]
