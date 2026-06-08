from django.db import models

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=50)
    desc = models.TextField()
    price = models.IntegerField()
    image = models.ImageField(upload_to="images") #need pip install  pillow
    
    def __str__(self):
        return self.title
    
    
    #python3 manage.py makemigrations
    #python3 manage.py 