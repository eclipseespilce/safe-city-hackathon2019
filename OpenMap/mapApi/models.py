from django.db import models

class Group(models.Model):
    name = models.CharField(max_length=100, blank=False)


class MapPoint(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    description = models.TextField()
    image_url = models.CharField(max_length=100, blank=False, default='')
    group = models.ForeignKey(Group, on_delete=models.CASCADE, related_name='+')

