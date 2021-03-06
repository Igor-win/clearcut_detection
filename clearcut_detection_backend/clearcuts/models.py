from django.contrib.gis.db import models
from django.contrib.postgres.fields import JSONField
from django.utils import timezone


class Zone(models.Model):
    def __str__(self):
        return f"Zone {self.id}"


class Tile(models.Model):
    tile_index = models.CharField(max_length=7, blank=False, null=False)
    is_tracked = models.SmallIntegerField(default=0, null=False)

    def __str__(self):
        return self.tile_index


class Clearcut(models.Model):
    image_date_previous = models.DateField(default=timezone.now)
    image_date_current = models.DateField(default=timezone.now)
    area = models.FloatField()
    forest = models.PositiveIntegerField(default=0)
    clouds = models.PositiveIntegerField(default=0)
    centroid = models.PointField()
    zone = models.ForeignKey(Zone, on_delete=models.CASCADE)
    mpoly = models.PolygonField()

    def __str__(self):
        return f"Clearcut {self.id}"


class TileInformation(models.Model):
    tile_name = models.CharField(max_length=7, blank=False, null=False)
    tile_index = models.CharField(max_length=5, blank=False, null=False)
    tile_date = models.DateField(default=timezone.now)

    tile_location = models.URLField(max_length=200, blank=True, null=True)
    source_tci_location = models.URLField(max_length=200, blank=True, null=True)
    source_b04_location = models.URLField(max_length=200, blank=True, null=True)
    source_b08_location = models.URLField(max_length=200, blank=True, null=True)
    source_b8a_location = models.URLField(max_length=200, blank=True, null=True)
    source_b11_location = models.URLField(max_length=200, blank=True, null=True)
    source_b12_location = models.URLField(max_length=200, blank=True, null=True)
    source_clouds_location = models.URLField(max_length=200, blank=True, null=True)
    model_tiff_location = models.URLField(max_length=200, blank=True, null=True)

    tile_metadata_hash = models.CharField(max_length=32, default=0, blank=True, null=True)
    cloud_coverage = models.FloatField(default=0, blank=False, null=False)
    mapbox_tile_id = models.CharField(max_length=32, blank=True, null=True)
    mapbox_tile_name = models.CharField(max_length=32, blank=True, null=True)
    mapbox_tile_layer = models.CharField(max_length=32, blank=True, null=True)
    coordinates = models.PolygonField(blank=True, null=True)

    objects = models.Manager()


class RunUpdateTask(models.Model):
    tile_index = models.ForeignKey(Tile, on_delete=models.CASCADE)
    path_type = models.SmallIntegerField(default=0, null=False)
    path_img_0 = models.URLField(max_length=200, blank=False, null=False)
    path_img_1 = models.URLField(max_length=200, blank=False, null=False)
    image_date_0 = models.DateField(blank=False, null=False)  # TODO
    image_date_1 = models.DateField(blank=False, null=False)  # TODO
    result = JSONField(null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_started = models.DateTimeField(null=True, default=None)
    date_finished = models.DateTimeField(null=True, default=None)

    class Meta:
        db_table = 'clearcuts_run_update_task'
