from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Person)
admin.site.register(Item)
admin.site.register(Selection)
admin.site.register(ItemCategory)