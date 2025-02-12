from django.shortcuts import render

def index(request):
    return render(request , 'website/index.html')

def about_me(request):
    return render(request , 'website/about.html')

def contact_me(request):
    return render(request , 'website/contact.html')

def my_resume(request):
    return render(request , 'website/resume.html')

def my_services(request):
    return render(request , 'website/services.html')

def my_portfolio(request):
    return render(request , 'website/portfolio.html')


