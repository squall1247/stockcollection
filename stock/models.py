from django.db import models
from django.contrib import admin
from django.urls import reverse

# Create your models here.
class Stock(models.Model):
    stock_name = models.CharField(max_length = 20)
    stock_price = models.DecimalField(max_digits = 5, decimal_places=0)
        
    def __str__(self):
        return self.stock_name
        
    class Meta:
        db_table = "stock"
    
    #it will be call by edit.py when using class based view
    def get_absolute_url(self):
        return reverse("stocks:stock_id", kwargs={"pk": self.id})
        
@admin.register(Stock)
class StockAdmin(admin.ModelAdmin):
	list_display = [field.name for field in Stock._meta.fields]