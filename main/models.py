from django.db import models

class Event(models.Model):
    Name = models.CharField(max_length=50)
    Description = models.CharField(max_length=500)
    Location = models.CharField(max_length=50)
    fromDate = models.DateField()
    fromTime = models.TimeField()
    toDate = models.DateField()
    toTime = models.TimeField()
    regEndDate = models.DateField()
    regEndTime = models.TimeField()
    posterLink = models.CharField(max_length=10000, blank=True)
    hostEmail = models.EmailField()
    hostPW = models.CharField(max_length=50)
    status = models.IntegerField(default=1)
    def __str__(self):
        return self.Name

class Participant(models.Model):
    Name = models.CharField(max_length=50)
    Contact = models.CharField(max_length=10)
    Email = models.EmailField()
    proofLink = models.CharField(max_length=10000, blank=True)
    Type = models.CharField(max_length=10)
    Tickets = models.IntegerField()
    EventID = models.IntegerField()
    def __str__(self):
        return self.Name