from django.contrib import admin
from .models import Product, Customer


# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    readonly_fields = ("slug",)
    list_filter = ("name",)
    list_display = ('id',"name")
    # prepopulated_fields = {"slug": ("name",)}

admin.site.register(Product, ProductAdmin)
admin.site.register(Customer)

