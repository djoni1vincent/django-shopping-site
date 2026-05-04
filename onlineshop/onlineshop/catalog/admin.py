from django.contrib import admin

from .models import Brand, Category, Product

# Register your models here.


class ProductInLine(admin.TabularInline):
    extra = 0
    model = Product
    show_change_link = True
    readonly_fields = ["created_at", "updated_at", "category"]
    fields = ["name", "category", "price", "stock"]


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name"]
    inlines = [ProductInLine]


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ["name", "brand", "category", "price", "stock"]


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ["name", "products_count"]
    inlines = [ProductInLine]

    def products_count(self, obj):
        return obj.product_set.count()

    products_count.short_description = "Quantity"
