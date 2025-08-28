from django.db import models

# Create your models here.


class Venue(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    capacity = models.IntegerField()

    def __str__(self):
        return self.name

class Event(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateField()
    start_time = models.TimeField()
    venue = models.ForeignKey(Venue, on_delete=models.CASCADE, related_name='events')

    def __str__(self):
        return self.title + " at " + self.venue.name