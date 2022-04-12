from django.contrib import admin

# Register your models here.
from .models import Product, Order, Customer, ProductOrder

class CustomerAdmin(admin.ModelAdmin):
    list_display = ('email', 'first_name', 'last_name')

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'image', 'price')

class ProductOrderAdmin(admin.ModelAdmin):
    list_display = ('Order', 'product', 'quantity')

class OrderAdmin(admin.ModelAdmin):
    list_display = ('Product', 'Customer', 'date', 'Status')




admin.site.register(Product, ProductAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(Customer, CustomerAdmin)
admin.site.register(ProductOrder, ProductOrderAdmin)

