from .views import *
from django.contrib.auth import views as auth_views
from django.urls import path

from django.contrib import admin

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path("", index, name="index"),

    path('admin/', admin.site.urls),           # Admin panel
    path('', index, name='home'),        # Home page
    path('about/', about, name='about'), # About page
    path('message/<str:name>', aboutmessage, name='aboutmessage'), # About page

    path('programs/', programs, name='programs'), # About page
    path('notices/', notices, name='notices'), # About page


    path('notice/<int:id>', notice, name='notice'), # About page
    path('program/<int:id>', program, name='program'), # About page


    path('contact/', contact, name='contact'), # Contact page
    path('register/', register, name='register'), # Contact page

]

