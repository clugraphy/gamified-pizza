from django.contrib import admin
from orders.models import Product, Category


# Register your models here.


class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name", "slug"]
    prepopulated_fields = {"slug": ("name",)}


admin.site.register(Category, CategoryAdmin)


class ProductAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "slug",
        "price",
        "stock",
        "available",
        "pizzereum",
        "created_at",
        "updated_at",
    ]
    list_filter = ["available", "created_at", "updated_at"]
    search_fields = ["name"]
    list_editable = ["price", "stock", "available", "pizzereum"]
    prepopulated_fields = {"slug": ("name",)}


admin.site.register(Product, ProductAdmin)
