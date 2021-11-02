from django.db import models
from django.contrib.auth.models import User

class Advisor(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to = "pics")


class Booking(models.Model):
    advisor = models.ForeignKey(Advisor, on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    booking_time = models.DateTimeField()