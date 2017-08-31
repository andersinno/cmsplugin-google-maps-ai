# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-07-20 03:10
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cms', '0016_auto_20160608_1535'),
    ]

    operations = [
        migrations.CreateModel(
            name='GoogleMapsAddressEmbed',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='cmsplugin_google_maps_ai_googlemapsaddressembed', serialize=False, to='cms.CMSPlugin')),
                ('street_address', models.CharField(blank=True, max_length=128, verbose_name='street address')),
                ('postal_code', models.CharField(blank=True, max_length=24, verbose_name='postal code')),
                ('city', models.CharField(blank=True, max_length=128, verbose_name='city')),
                ('country', models.CharField(blank=True, max_length=128, verbose_name='country')),
                ('embed_height', models.PositiveSmallIntegerField(default=250, help_text='Height of the map embed in pixels.', verbose_name='embed height')),
                ('zoom_level', models.PositiveSmallIntegerField(default=10, help_text='Map zoom level. Values range from 0 (the whole world) to 21 (individual buildings).', verbose_name='zoom level')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
    ]