from django.contrib import admin
from .models import Product, Customer, Address, Country


# Register your models here.
# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    readonly_fields = ("slug",)
    list_filter = ("name","customer")
    list_display = ('id',"name")
    # prepopulated_fields = {"slug": ("name",)}

class CustomerAdmin(admin.ModelAdmin):
    list_display = ('id',"name",'avatar')


admin.site.register(Product, ProductAdmin)
admin.site.register(Customer,CustomerAdmin)
admin.site.register(Address)
admin.site.register(Country)

