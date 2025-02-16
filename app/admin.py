from django.contrib import admin
from .models import Customer, Product, Cart, OrderPlaced
from django.utils.html import format_html
from django.urls import reverse

@admin.register(Customer)
class CustomerModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'name', 'locality', 'city', 'zipcode', 'state']
    search_fields = ['name', 'city']
    list_filter = ['state']

@admin.register(Product)
class ProductModelAdmin(admin.ModelAdmin): 
    list_display = ['id', 'title', 'brand', 'category', 'selling_price', 'discounted_price', 'product_image']
    search_fields = ['title', 'brand']
    list_filter = ['category']

@admin.register(Cart)
class CartModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'product', 'quantity']
    search_fields = ['user__username']
    list_filter = ['product']

@admin.register(OrderPlaced)
class OrderPlacedModelAdmin(admin.ModelAdmin): 
    list_display = ['id', 'user', 'customer','customer_info', 'product','product_info', 'quantity', 'ordered_date', 'status']

    def customer_info(self, obj):
        link = reverse("admin:app_customer_change", args=[obj.customer.pk])
        return format_html('<a href="{}">{}</a>', link, obj.customer. name)

    def product_info(self, obj):
        link = reverse("admin:app_product_change", args=[obj.product.pk])
        return format_html('<a href="{}">{}</a>', link, obj.product.title)  



