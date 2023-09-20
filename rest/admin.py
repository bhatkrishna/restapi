from django.contrib import admin
from .models import Students

class StudentsAdmin(admin.ModelAdmin):
    list_display = ['name','roll_no']

admin.site.register(Students, StudentsAdmin)

# Register your models here.
