from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from website.forms import NameForm, ContactForm, newsletterForm
from django.contrib import messages

def index_view(request):
    return render(request, 'website/index.html')

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()  # متد save بازنویسی شده مقدار name را به "ناشناس" تغییر می‌دهد
            messages.success(request, 'Submitted Successfully!')
        else:
            messages.error(request, 'There is an Error!')
    else:
        form = ContactForm()
        
    return render(request, 'website/contact.html', {'form': form})

def newsletter_view(request):
    if request.method == 'POST':
        form = newsletterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Newsletter subscribed successfully!')
            return HttpResponseRedirect('/')
        else:
            messages.error(request, 'Subscription failed!')

    return HttpResponseRedirect('/')

def about_view(request):
    return render(request, 'website/about.html')
