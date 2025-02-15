from django.contrib import admin
from .models import Notice, Career, Contact, Register, Departments, Academics, Programs

# Registering models for the admin interface
@admin.register(Notice)
class NoticeAdmin(admin.ModelAdmin):
    list_display = ('title', 'pub_date')
    search_fields = ('title', 'head')



@admin.register(Programs)
class ProgramsAdmin(admin.ModelAdmin):
    list_display = ('name', 'about')


@admin.register(Career)
class CareerAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'contact')
    search_fields = ('name', 'email')

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'address')
    search_fields = ('name', 'address')

@admin.register(Register)
class RegisterAdmin(admin.ModelAdmin):
    list_display = ('student_name', 'dob', 'gender', 'email', 'phone', 'grade')
    search_fields = ('student_name', 'email', 'phone')
    list_filter = ('gender', 'grade')

@admin.register(Departments)
class DepartmentsAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title',)

@admin.register(Academics)
class AcademicsAdmin(admin.ModelAdmin):
    list_display = ('name', 'department', 'forewords')
    search_fields = ('name', 'department__title')
    list_filter = ('department',)
