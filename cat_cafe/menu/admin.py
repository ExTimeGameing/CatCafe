from django.contrib import admin
from .models import Category, MenuItem, Order, OrderItem, Client, Payment, Cat

admin.site.register(Category)
admin.site.register(MenuItem)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Client)
admin.site.register(Payment)
admin.site.register(Cat)
