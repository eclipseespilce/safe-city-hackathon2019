from django.db import models


class Group(models.Model):
    name = models.CharField(max_length=100, blank=False)
    description = models.TextField()

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
    image_url = models.CharField(max_length=100, blank=False, default='')
    group = models.ForeignKey(Group, on_delete=models.CASCADE, related_name='map_points')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='map_points')
    status = models.ForeignKey(Status, on_delete=models.CASCADE, related_name='map_points')
    latitude = models.FloatField()
    longitude = models.FloatField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{}".format(self.description)