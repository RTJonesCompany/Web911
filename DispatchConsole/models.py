from django.db import models

# Create your models here.
class UnitType(models.Model):
    description = models.CharField(max_length=255)

    def __str__(self):
        return self.description

class Unit(models.Model):
    name = models.CharField(max_length=255)
    handle = models.CharField(max_length=30)
    description = models.TextField()
    type = models.ForeignKey(UnitType, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Location(models.Model):
    address = models.CharField(max_length=255)
    addressInfo = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=2)
    county = models.CharField(max_length=255)
    zipcode = models.CharField(max_length=10)
    lat = models.DecimalField(max_digits=8, decimal_places=3)
    lng = models.DecimalField(max_digits=8, decimal_places=3)
    def __str__(self):
        return self.address
class Message(models.Model):
    data = models.TextField()
    timestamp = models.DateTimeField(auto_now='true')
    def __str__(self):
         return '[ %s ] %s' % (self.timestamp, self.data)


class IncidentStatus(models.Model):
    description = models.CharField(max_length=255)
    def __str__(self):
        return self.description

class IncidentNature(models.Model):
    description = models.CharField(max_length=255)
    code = models.CharField(max_length=4)
    def __str__(self):
        return self.description

class Incident(models.Model):
    location = models.ForeignKey(Location)
    nature = models.ForeignKey(IncidentNature)
    opened = models.DateTimeField(auto_now='true')
    closed = models.DateTimeField()
    messages = models.ManyToManyField(Message)
    units = models.ManyToManyField(Unit)

    def __str__(self):
        return self.location.address
        
# this class is not needed. I moved the messages into the incident instead of having a seprate table track it
#class IncidentMessage(models.Model):
            #incident = models.ManyToManyField(Incident)
            #message = models.ManyToManyField(Message)
