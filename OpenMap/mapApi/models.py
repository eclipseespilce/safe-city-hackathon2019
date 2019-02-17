import os

from django.db import models
from django.utils.deconstruct import deconstructible


@deconstructible
class PathAndRenameCompetition(object):
    def __init__(self, sub_path):
        self.path = sub_path

    def __call__(self, instance, filename):
        expansion = filename.split('.')[-1]
        if type(instance) is Group:
            filename = '{}_{}.{}'.format(instance.pk, instance.name, expansion)
            return os.path.join(self.path, filename)


class Group(models.Model):
    name = models.CharField(max_length=100, blank=False)
    description = models.TextField()
    image = models.ImageField(upload_to=PathAndRenameCompetition("group-images/"), max_length=500)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=100, blank=False)
    description = models.TextField()

    def __str__(self):
        return self.name


class Status(models.Model):
    name = models.CharField(max_length=100, blank=False)
    description = models.TextField()

    def __str__(self):
        return self.name


class MapPoint(models.Model):
    description = models.TextField()
    image_url = models.CharField(max_length=100, blank=True, default='')
    group = models.ForeignKey(Group, on_delete=models.CASCADE, related_name='map_points')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='map_points')
    status = models.ForeignKey(Status, on_delete=models.CASCADE, related_name='map_points')
    latitude = models.FloatField()
    longitude = models.FloatField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{}".format(self.description)
