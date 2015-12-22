# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FavoriteDoctors',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
        ),
        migrations.CreateModel(
            name='Insurance',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50, choices=[(b'Aetna', b'Aetna'), (b'Cigna', b'Cigna'), (b'Medicaid', b'Medicaid'), (b'Medicare', b'Medicare'), (b'Tricare', b'Tricare'), (b'Blue', b'Blue'), (b'United', b'United')])),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('rating', models.IntegerField()),
                ('comment', models.TextField()),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('name', models.CharField(default=b'', max_length=30)),
                ('username', models.EmailField(max_length=254, serialize=False, primary_key=True)),
                ('password', models.CharField(max_length=256)),
                ('type', models.CharField(max_length=10, choices=[(b'Admin', b'Admin'), (b'Patient', b'Patient'), (b'Doctor', b'Doctor')])),
            ],
        ),
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('phoneNumber', models.CharField(default=b'', max_length=15)),
                ('officeHours', models.CharField(default=b'', max_length=100)),
                ('speciality', models.CharField(max_length=30, choices=[(b'Primary Care', b'Primary Care'), (b'Dentist', b'Dentist'), (b'Dermatologist', b'Dermatologist'), (b'ENT', b'ENT'), (b'Eye Doctor', b'Eye Doctor'), (b'Psychiatrist', b'Psychiatrist'), (b'Orthopedist', b'Orthopedist')])),
                ('rating', models.FloatField()),
                ('availability', models.DateField(default=b'')),
                ('state', models.CharField(default=b'', max_length=20)),
                ('city', models.CharField(default=b'', max_length=30)),
                ('zip', models.CharField(default=b'', max_length=30)),
                ('street', models.CharField(default=b'', max_length=50)),
                ('education', models.TextField(default=b'')),
                ('awards', models.TextField(default=b'')),
                ('experience', models.TextField(default=b'')),
                ('username', models.OneToOneField(primary_key=True, serialize=False, to='website.User')),
            ],
        ),
        migrations.AddField(
            model_name='review',
            name='patient',
            field=models.ForeignKey(to='website.User'),
        ),
        migrations.AddField(
            model_name='favoritedoctors',
            name='patient',
            field=models.ForeignKey(to='website.User'),
        ),
        migrations.AddField(
            model_name='review',
            name='doctor',
            field=models.ForeignKey(to='website.Doctor'),
        ),
        migrations.AddField(
            model_name='insurance',
            name='doctor',
            field=models.ForeignKey(to='website.Doctor'),
        ),
        migrations.AddField(
            model_name='favoritedoctors',
            name='doctor',
            field=models.ForeignKey(to='website.Doctor'),
        ),
    ]
