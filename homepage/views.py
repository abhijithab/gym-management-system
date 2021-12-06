from django.shortcuts import render




def home(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about_us.html')

def classdetails(request):
    return render(request,'details.html')

def services(request):
    return render(request,'services.html')

def team(request):
    return render(request,'team.html')

def contact(request):
    return render(request,'contact.html')

def timetable(request):
    return render(request,'timetable.html')

def calculator(request):
    return render(request,'calculator.html')

def gallery(request):
    return render(request,'gallery.html')

def blog(request):
    return render(request,'blog.html')

def error(request):
    return render(request,'404.html')