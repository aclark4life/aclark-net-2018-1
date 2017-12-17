from .forms import ContactForm
from django.conf import settings
from django.contrib import messages
from django.core.mail import send_mail
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.utils import timezone
import random
import requests

# Create your views here.

BASE_URL = 'https://db.aclark.net'
CLIENT_URL = '%s/api/clients/?format=json' % BASE_URL
SERVICE_URL = '%s/api/services/?format=json' % BASE_URL
TESTIMONIAL_URL = '%s/api/testimonials/?format=json' % BASE_URL
PROFILE_URL = '%s/api/profiles/?format=json' % BASE_URL


def about(request):
    context = {}
    context['active_nav'] = 'about'
    return render(request, 'about.html', context)


def page(request, slug=None):
    context = {}
    return render(request, 'page.html', context)


def blog(request):
    context = {}
    context['active_nav'] = 'more'
    return render(request, 'blog.html', context)


def book(request):
    context = {}
    context['active_nav'] = 'more'
    return render(request, 'book.html', context)


def clients(request):
    context = {}
    clients = requests.get(CLIENT_URL).json()
    context['clients'] = clients
    context['active_nav'] = 'clients'
    return render(request, 'clients.html', context)


def community(request):
    context = {}
    context['active_nav'] = 'more'
    return render(request, 'community.html', context)


def contact(request):
    context = {}
    now = timezone.datetime.now
    msg = 'Sent, thank you. Please expect a reply within 24 hours. '
    msg += 'For urgent matters please contact Alex Clark <aclark@aclark.net>.'
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            message = form.cleaned_data['message']
            sender = form.cleaned_data['email']
            message = '\n'.join([message, sender])
            recipients = [settings.EMAIL_FROM]
            subject = settings.EMAIL_SUBJECT % now().strftime(
                '%m/%d/%Y %H:%M:%S')
            send_mail(subject, message, settings.EMAIL_FROM, recipients)
            messages.add_message(request, messages.SUCCESS, msg)
            return HttpResponseRedirect(reverse('home'))
    else:
        form = ContactForm()
    context['form'] = form
    context['active_nav'] = 'contact'
    return render(request, 'contact.html', context)


def history(request):
    context = {}
    context['active_nav'] = 'more'
    return render(request, 'history.html', context)


def home(request):
    context = {}
    context['show_carousel'] = True
    testimonials = requests.get(TESTIMONIAL_URL).json()
    context['testimonial'] = random.choice(testimonials)
    return render(request, 'home.html', context)


def location(request):
    context = {}
    context['active_nav'] = 'more'
    return render(request, 'location.html', context)


def opensource(request):
    context = {}
    context['active_nav'] = 'more'
    return render(request, 'opensource.html', context)


def projects(request):
    context = {}
    context['active_nav'] = 'projects'
    return render(request, 'projects.html', context)


def services(request):
    context = {}
    services = requests.get(SERVICE_URL).json()
    context['services'] = services
    context['active_nav'] = 'services'
    return render(request, 'services.html', context)


def testimonials(request):
    context = {}
    testimonials = requests.get(TESTIMONIAL_URL).json()
    context['testimonials'] = testimonials
    context['active_nav'] = 'testimonials'
    return render(request, 'testimonials.html', context)


def team(request):
    context = {}
    profiles = requests.get(PROFILE_URL).json()
    context['profiles'] = profiles
    context['active_nav'] = 'team'
    return render(request, 'team.html', context)


def now(request):
    return HttpResponseRedirect('http://blog.aclark.net/now')
