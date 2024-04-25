from django.db import models

# Create your models here.


class Hyd_job(models.Model):
    date=models.DateField()
    company=models.CharField(max_length=30)
    title=models.CharField(max_length=30)
    Eligibilty=models.CharField(max_length=30)
    Address=models.CharField(max_length=100)
    Email=models.EmailField()
    Phone=models.BigIntegerField()

class Pune_jobs(models.Model):
    date=models.DateField()
    company=models.CharField(max_length=30)
    title=models.CharField(max_length=30)
    Eligibilty=models.CharField(max_length=30)
    Address=models.CharField(max_length=100)
    Email=models.EmailField()
    Phone=models.BigIntegerField()

class Bang_jobs(models.Model):
    date=models.DateField()
    company=models.CharField(max_length=30)
    title=models.CharField(max_length=30)
    Eligibilty=models.CharField(max_length=30)
    Address=models.CharField(max_length=100)
    Email=models.EmailField()
    Phone=models.BigIntegerField()