from django.contrib import admin
from .models import Product ,Card
# Register your models here.
# admin.site.register(Product) 

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id','title','desc','price','image']

@admin.register(Card)
class CardAdmin(admin.ModelAdmin):
    list_display = ['id','name','collage']