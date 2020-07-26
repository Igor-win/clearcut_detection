# Generated by Django 2.2.14 on 2020-07-20 07:16

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('clearcuts', '0006_02'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tile_index', models.CharField(max_length=7)),
                ('is_tracked', models.SmallIntegerField(default=0)),
            ],
        ),
        migrations.AlterField(
            model_name='clearcut',
            name='image_date_current',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='clearcut',
            name='image_date_previous',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='tileinformation',
            name='tile_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.RunSQL('DELETE FROM clearcuts_tileinformation'),
        migrations.CreateModel(
            name='RunUpdateTask',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('path_type', models.SmallIntegerField(default=0)),
                ('path_img_0', models.URLField()),
                ('path_img_1', models.URLField()),
                ('image_date_0', models.DateField()),
                ('image_date_1', models.DateField()),
                ('result', django.contrib.postgres.fields.jsonb.JSONField(null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_started', models.DateTimeField(default=None, null=True)),
                ('date_finished', models.DateTimeField(default=None, null=True)),
                ('tile_index', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clearcuts.Tile')),
            ],
            options={
                'db_table': 'clearcuts_run_update_task',
            },
        ),
    ]
