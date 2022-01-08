from django.contrib import admin

# Register your models here.
from .models import BillingAddress, Item, OrderItem, Order, Payment

admin.site.register(Item)
admin.site.register(OrderItem)
admin.site.register(Order)
admin.site.register(BillingAddress)
admin.site.register(Payment)