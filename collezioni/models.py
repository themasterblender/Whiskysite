from django.db import models
from django.utils import timezone

class Collezione(models.Model):
    owner = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=40)
    text = models.TextField(null=True)
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class Category(models.Model):
    name = models.CharField(max_length=20)    
    def __str__(self):
        return self.name

class Bottle(models.Model):
    collezione = models.ForeignKey('Collezione', on_delete=models.CASCADE)
    whisky_type = models.ForeignKey('Category', on_delete=models.CASCADE)
    name = models.CharField(max_length=40)
    distillery = models.CharField(max_length=40, null=True, blank=True)
    bottler = models.CharField(max_length=40)
    age = models.SmallIntegerField(null=True, blank=True)
    year_bottled = models.DecimalField(max_digits=4, decimal_places=0, null=True, blank=True)
    purchased_date = models.DateField()
    purchased_place = models.CharField(max_length=40, null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2, default=0)
    bottle_code = models.CharField(max_length = 20, null=True, blank=True)
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.name


