from django.shortcuts import render
from django.http import HttpResponse
from website.forms import NameForm

def index_view(request):
    return render(request, 'website/index.html')

def contact_view(request):
    return render(request, 'website/contact.html')

def about_view(request):
    return render(request, 'website/about.html')
