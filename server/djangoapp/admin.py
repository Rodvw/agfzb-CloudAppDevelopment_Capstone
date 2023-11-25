from django.contrib import admin
from .models import CarMake, CarModel  # Asegúrate de importar tus modelos aquí

# CarModelInline class
class CarModelInline(admin.StackedInline):
    model = CarModel
    extra = 1



# CarModelAdmin class
class CarModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'year')
    list_filter = ['year']
    search_fields = ['name', 'type']

# CarMakeAdmin class with CarModelInline
class CarMakeAdmin(admin.ModelAdmin):
    inlines = [CarModelInline]  # Esto añade la sección de CarModel al admin de CarMake
    list_display = ('name', 'desc')  # Ajusta estos campos según tu modelo CarMake

# Registrar modelos aquí
admin.site.register(CarMake, CarMakeAdmin)
admin.site.register(CarModel, CarModelAdmin)
