from django.contrib import admin

from .models import Category, Order, OrderItem, Product, UserProfile

# Register your models here.

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(UserProfile)
admin.site.register(Order)
admin.site.register(OrderItem)
