from django.contrib import admin
from .models import Forms

# Register your models here.


@admin.register(Forms)
class FormAdmin(admin.ModelAdmin):
    list_display = ('name',)
