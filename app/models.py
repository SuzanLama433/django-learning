from django.db import models

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=50)
    desc = models.TextField()
    price = models.IntegerField()
    image = models.ImageField(upload_to="images") #need pip install  pillow
    
    def __str__(self):
        return self.title
    
class Card(models.Model):
    collage = models.CharField(max_length=20)
    image = models.ImageField(upload_to="images")
    name = models.CharField(max_length=20)
    course = models.CharField(max_length=20)
    phone = models.IntegerField()
    email = models.CharField(max_length=50)
    valid = models.IntegerField()
    
    def __str__(self):
        return self.name  
    
    
    #python3 manage.py makemigrations
    #python3 manage.py migrate