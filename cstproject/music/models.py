from django.db import models


# Create your models here.
class Book(models.Model):
    title = models.CharField("titles", max_length = 60, default = '')
    price = models.DecimalField("myprice", max_digits = 6, decimal_places = 2, default = '')
