from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, HttpResponse
from . import forms
from django.views.decorators import require_http_methods
from django.contrib.auth import authenticate, login, logout
from django.urls.utils import reverse
# from .models import model, model
from django.contrib.auth.decorators import login_required


# Create your views here.

def index(request):
    return render(request, 'index.html')


def other_page(request):
    relativedict = {"wtf": 'WTF', 'number': 666}
    return render(request, 'other.html', context=relativedict)


def relative(request):
    relativedict = {"wtf": 'WTF', 'number': 100, 'hello': 'hello you motherfucking piece of shit'}
    return render(request, 'other.html', context=relativedict)


# @require_http_methods(['POST'])
def login_page(request):
    context = {"user_login": forms.UserForm}
    if request.method == 'POST':

        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
        HttpResponseRedirect(request, reverse('index'), context={})

    else:
        render(request, "relative.html", context=context)


def register(request):
    registered = False

    context = {"user_form": forms.UserForm, "profile_form": forms.ProfileForm, "registered": registered}
    if request.method == 'POST':
        user_regis = UserForm(request.POST)
        profile_form = ProfileForm(request.POST)
        if profile_form.is_valid and user_regis.is_valid:
            user_regis.save()
            user_regis.set_password(user_regis.password)
            user_regis.save()

            profile = profile_form.save(commit=False)

            profile.user = user_regis

            # Check if they provided a profile picture
            if 'profile_pic' in request.FILES:
                print('found it')
                # If yes, then grab it from the POST form reply
                profile.profile_pic = request.FILES['profile_pic']

            profile.save()
            registered = True

        else:
            print(user_regis.errors, profile_form.errors)

    # This is the render and context dictionary to feed
    # back to the registration.html file page.
    return render(request, 'basic_app/login.html', context=context)

