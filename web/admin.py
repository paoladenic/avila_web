from django.contrib import admin
from .models import Product, Category, Condition

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']

class ConditionAdmin(admin.ModelAdmin):
    list_display = ['name']

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'condition', 'description1', 'description2', 'description3', 'description4', 'description5', 'description6', 'price']

admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Condition, ConditionAdmin)