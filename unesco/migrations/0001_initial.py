# Generated by Django 3.1 on 2020-09-09 15:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Iso',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='States',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Site',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('description', models.CharField(max_length=5000)),
                ('justification', models.CharField(max_length=5000)),
                ('year', models.IntegerField(null=True)),
                ('longitude', models.FloatField(null=True)),
                ('latitude', models.FloatField(null=True)),
                ('area_hectares', models.FloatField(null=True)),
                ('States', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='unesco.states')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='unesco.category')),
                ('iso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='unesco.iso')),
                ('region', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='unesco.region')),
            ],
        ),
    ]
