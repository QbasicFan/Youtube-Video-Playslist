from django.contrib import admin

# Register your models here.

from .models import bookMark, catego

admin.site.register(bookMark)
admin.site.register(catego)
