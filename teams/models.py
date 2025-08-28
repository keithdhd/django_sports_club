from django.db import models

# Create your models here.
class Team(models.Model):
    name = models.CharField(max_length=100)
    sport = models.CharField(max_length=100)
    founded_year = models.IntegerField()

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']


class Player(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    position = models.CharField(max_length=50)
    team = models.ForeignKey(Team, related_name='players', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"