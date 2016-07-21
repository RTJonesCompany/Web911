from django.db import models

# Create your models here.
class UnitType(models.Model):
    description = model.CharField(max_length=255)

    def __str__(self):
        return self.description

class Unit(models.Model):
    name = model.CharField(max_length=255)
    handle = model.CharField(max_length=30)
    description = model.TextField()
    type = model.ForeignKey(UnitType, on_delete=model.CASCADE)

    def __str__(self):
        return self.name

class Location(models.Model):
    address = model.CharField(max_length=255)
    addressInfo = model.CharField(max_length=255)
    city = model.CharField(max_length=255)
    state = model.CharField(max_length=2)
    county = model.CharField(max_length=255)
    zipcode = model.CharField(max_length=10)
    lat = models.DecimalField(max_digits=8, decmial_places=3)
    lng = models.DecimalField(max_digits=8, decmial_places=3)



class IncidentStatus(models.Model):
    description = model.CharField(max_length=255)
    def __str__(self):
        return self.description

class IncidentNature(models.Model):
    description = model.CharField(max_length=255)
    def __str__(self):
        return self.description

class Incident(model.Models):
    location = models.ForeignKey(Location)
    Nature = models.ForeignKey(IncidentNature)
    opened = models.DateTimeField(auto_now='true')
    closed = models.DateTimeField()

class Messages(models.Model)
    data = models.TextField()
    timestamp = models.DateTimeField(auto_now='true')

class IncidentMessage(models.Model)
    incident = models.models.ManyToManyField(Incident)
    message = models.ManyToManyField(Message)
    
