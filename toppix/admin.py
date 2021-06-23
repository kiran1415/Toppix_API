from django.contrib import admin
from .models import Tags,Category,SubCategory,Toppix
# Register your models here.

admin.site.register(Tags)
admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(Toppix)