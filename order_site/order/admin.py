from django.contrib import admin

# Register your models here.
from .models import Product, Order, Customer, ProductOrder, Status

class CustomerAdmin(admin.ModelAdmin):
    list_display = ('email')

admin.site.register(Product)
admin.site.register(Order)
admin.site.register(Customer)
admin.site.register(ProductOrder)
admin.site.register(Status)