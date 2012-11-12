from django.db import models



class Nonprofit(models.Model):
    url = models.CharField(max_length=1200, primary_key=True)
    filename = models.CharField(max_length=100,blank=True)
    doctype = models.CharField(max_length=100,blank=True)
    year = models.CharField(max_length=100,blank=True)
    idstr = models.CharField(max_length=100,blank=True)
    text = models.CharField(max_length=1200,blank=True)
    formtype = models.CharField(max_length=100,blank=True)
    date = models.CharField(max_length=100,blank=True)
    size = models.CharField(max_length=100,blank=True)
    assetts = models.DecimalField(max_digits=20,decimal_places=2)
    hashstr = models.CharField(max_length=1200,blank=True)
    md5 = models.CharField(max_length=1200,blank=True)





