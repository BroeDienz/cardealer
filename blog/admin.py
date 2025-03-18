from django.contrib import admin
from .models import Car

# Register your models here.
class CarAdmin(admin.ModelAdmin):
    list_display = ('register', 'make', 'model', 'price', 'year', 'vin')
    search_fields = ('make', 'model', 'vin')
    list_filter = ('make', 'model', 'year')
    ordering = ('make', 'model')
    # readonly_fields = ('register', 'make', 'model', 'price', 'year', 'vin')
    list_per_page = 20
    
admin.site.register(Car, CarAdmin)  # Register the Car model with the CarAdmin options