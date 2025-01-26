from django.contrib import admin
from .models import Notice, Career, Contact, Register, Departments, Academics

# Registering models for the admin interface
@admin.register(Notice)
class NoticeAdmin(admin.ModelAdmin):
    list_display = ('title', 'pub_date')
    search_fields = ('title', 'head')

@admin.register(Career)
class CareerAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'contact')
    search_fields = ('name', 'email')

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('Name', 'email', 'phone', 'subject')
    search_fields = ('Name', 'email', 'subject')

@admin.register(Register)
class RegisterAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'phone', 'course')
    search_fields = ('first_name', 'last_name', 'email', 'course')

@admin.register(Departments)
class DepartmentsAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title',)

@admin.register(Academics)
class AcademicsAdmin(admin.ModelAdmin):
    list_display = ('name', 'department', 'qualification')
    search_fields = ('name', 'department__title')
    list_filter = ('department',)
