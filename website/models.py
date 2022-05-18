from django.db import models



class SampleModel(models.Model):
    title = models.CharField(max_length = 100)
    address = models.CharField(max_length = 100)
    area = models.CharField(max_length = 100)
    task = models.CharField(max_length = 100)
    date = models.CharField(max_length = 100)
    price = models.CharField(max_length = 100)
    name = models.CharField(max_length = 100)
    phone = models.CharField(max_length = 100)

    def __str__(self):
        return self.title