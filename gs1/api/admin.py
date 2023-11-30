from django.contrib import admin
from .models import Student
# Register your models here.

#registering student model with our django admin using @admin decorator
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'roll', 'city']