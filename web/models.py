from django.db import models

class Category(models.Model):
    name= models.CharField(max_length=50)

    @staticmethod
    def get_all_categories():
        return Category.objects.all()
    def __str__(self):
        return self.name
    
class Condition(models.Model):
    name= models.CharField(max_length=50)

    @staticmethod
    def get_all_conditions():
        return Condition.objects.all()
    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=255)
    category= models.ForeignKey(Category,on_delete=models.CASCADE)
    condition = models.ForeignKey(Condition,on_delete=models.CASCADE)
    description1 = models.CharField(max_length=255)
    description2 = models.CharField(max_length=255)
    description3 = models.CharField(max_length=255)
    description4 = models.CharField(max_length=255, blank=True)
    description5 = models.CharField(max_length=255, blank=True)
    description6 = models.CharField(max_length=255, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='products/')
    created_at = models.DateTimeField(auto_now_add=True)
 
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return f'/product/{self.name}/'

