from django.http import HttpResponse
from .models import *
from django.shortcuts import render
from .forms import SchoolRegistrationForm
from django.shortcuts import redirect
from django.contrib import messages

def register(request):
    if request.method == "POST":
        student_name = request.POST.get("student_name")
        dob = request.POST.get("dob")
        gender = request.POST.get("gender")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        address = request.POST.get("address")
        # Ensure dob is in YYYY-MM-DD format
        if not dob:
            return HttpResponse("Invalid Date of Birth", status=400)

        # Save to database
        Register.objects.create(
            student_name=student_name,
            dob=dob,
            gender=gender,
            email=email,
            phone=phone,
            address=address,
        )
        messages.success(request, "Register Submitted Successfully." )

        return redirect("/register")  # Redirect after successful registration

    return render(request, "register.html")

def index(request):
    programs = Programs.objects.all()
    notice = Notice.objects.all().order_by('-pub_date')
    context = {
        'programs': programs,
        'notice': notice
    }
    if request.method == "POST":
        name = request.POST.get("name")
        address = request.POST.get("address")
        phone = request.POST.get("contact")
        message = request.POST.get("message")

        Contact.objects.create(
            name=name,
            address=address,
            phone=phone,
            message=message,
        )
        messages.success(request, "Contact Submitted Successfully." )

        return redirect("/")
    return render(request, 'index.html', context)
    

def notice(request, id):
    notice = Notice.objects.filter(post_id= id)[0]
    context = {
        'notice': notice
    }
    return render(request, 'notice.html', context) 

def notices(request):
    notices = Notice.objects.all()
    context ={
        'notices': notices
    }
    return render(request, 'notices.html', context) 


def program(request, id):
    program = Programs.objects.filter(id= id)[0]
    related =  Programs.objects.all().exclude(id = program.id)[:3]

    context ={
        'program': program,
        'related': related
    }
    return render(request, 'program.html', context) 

def about(request):
    team = Academics.objects.all()
    context ={
        'team': team
    }
    return render(request, 'about.html', context) 

def programs(request):
    programs = Programs.objects.all()
    context ={
        'programs': programs
    }
    return render(request, 'programs.html', context) 


def contact(request):
    return render(request, 'index.html') 