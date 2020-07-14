# Generated by Django 2.2.3 on 2020-07-14 10:47

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('clearcuts', '0005_auto_20200625_0758'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clearcut',
            name='image_date_0',
            field=models.DateField(default=datetime.datetime(2020, 7, 14, 10, 47, 14, 482071, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='clearcut',
            name='image_date_1',
            field=models.DateField(default=datetime.datetime(2020, 7, 14, 10, 47, 14, 482107, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='tileinformation',
            name='model_tiff_location',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='tileinformation',
            name='source_b04_location',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='tileinformation',
            name='source_b08_location',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='tileinformation',
            name='source_b11_location',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='tileinformation',
            name='source_b12_location',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='tileinformation',
            name='source_b8a_location',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='tileinformation',
            name='source_clouds_location',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='tileinformation',
            name='source_tci_location',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='tileinformation',
            name='tile_date',
            field=models.DateField(default=datetime.datetime(2020, 7, 14, 10, 47, 14, 482944, tzinfo=utc)),
        ),
    ]
