from django.db import models


class ContactModel(models.Model):
  first_name = models.CharField(max_length=120)
  last_name = models.CharField(max_length=150)
  address = models.CharField(max_length=150)
  number = models.IntegerField()
  email = models.EmailField()



