from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required  # This will stop people who aren't logged in from accessing the page.
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from .forms import UserLoginForm, UserRegistrationForm
import re
# from django.template.context_processors import csrf(csrf should work with importing this)
# Create your views here.


def index(request):
    #  Return the index.html file (also see line 18 & 22 in urls.py)
    return render(request, 'index.html')  # Only add 'index.html' here and stick with 'index' below.


def login_input_fields(request, login_form):
    username = login_form['username'].value()
    password = login_form['password'].value()

    if username is None or username == "":
        messages.error(request, 'your username is required')
        return False
    if password is None or password == "":
        messages.error(request, 'password is required')
        return False

    return True


@login_required  # This decorator will check to see if the user is logged in before executing any more of the code.
def logout(request):
    #  Log user out
    auth.logout(request)
    messages.success(request, 'Successfully logged out')
    return redirect(reverse('index'))


def login(request):
    """Return a login page"""
    if request.user.is_authenticated:  # This if statement prevents people form accessing the login page by entering the URL into the URL bar.
        return redirect(reverse('index'))
    if request.method == 'POST':
        login_form = UserLoginForm(request.POST)  # Create an instance of the user login form and pass it in the request.post as an other constructor so
                                                  # a new login form will be created with the data posted from the form on the UI.

        if login_input_fields(request, login_form) is False:
            args = {'login_form': login_form, 'next': request.GET.get('next', '')}
            return render(request, 'login.html', args)

        if login_form.is_valid():
            user = auth.authenticate(username=request.POST['username'],
                                     password=request.POST['password'])

            if user:
                auth.login(user, request)
                messages.success(request, "Succesfully logged in")

                if request.GET and request.GET['next'] != '':
                    next = request.GET['next']
                    return HttpResponseRedirect(next)
                else:
                    return redirect(reverse('index'))  # This will redirect the user to a specific other page just so that they're not redirected back to the login page again when logged in.

            else:
                login_form.add_error("username", "Combination of username and password is incorrect")
    else:
        login_form = UserLoginForm()  # Otherwise, create an empty login.

    args = {'login_form': login_form, 'next': request.GET.get('next', '')}
    return render(request, 'login.html', args)


def registration_input_fields(request, registration_form):
    email = registration_form['email'].value()
    username = registration_form['username'].value()
    password1 = registration_form['password1'].value()
    password2 = registration_form['password2'].value()

    if email is None or email == "":
        messages.error(request, 'an email address is required')
        return False
    if not re.match(r"^[A-Za-z0-9\.\+_-]+@[A-Za-z0-9\._-]+\.[a-zA-Z]*$", email):
        messages.error(request, 'a valid email address is required')
        return False
    if username is None or username == "":
        messages.error(request, 'your username is required')
        return False
    if password1 is None or password1 == "":
        messages.error(request, 'password is required')
        return False
    if password2 is None or password2 == "":
        messages.error(request, 'confirmation password is required')
        return False

    if password1 != password2:
        messages.error(request, 'passwords do not match')
        return False

    return True


@login_required
def profile(request):
    """A view that displays the profile page of a logged in user"""
    return render(request, 'profile.html')


def registration(request):
    """Render registration page"""
    # if request.user.is_authenticated:
    #     return redirect(reverse('index'))

    if request.method == 'POST':
        registration_form = UserRegistrationForm(request.POST)

        if registration_input_fields(request, registration_form) is False:
            args = {'registration_form': registration_form}
            return render(request, 'registration.html', args)

        if registration_form.is_valid():
            registration_form.save()  # Because the model (user=) is already specified inside of the meta class in the registration form (forms.py) it's not needed to specify model again here.

            user = auth.authenticate(username=request.POST.get['username'],
                                     email=request.POST.get['email'],
                                     password=request.POST.get['password1'])

            if user:
                auth.login(user, request)
                messages.success(request, "Succesfully registered.")
                return redirect(reverse('index'))
            else:
                messages.error(request, "Unable to register this account")

    else:
        registration_form = UserRegistrationForm()  # Create an instance (variable)

    args = {'registration_form': registration_form}
    return render(request, 'registration.html', args)  # Pass render(request...) through a dictionary with registration_form as key and value (the instance).


def user_profile(request):
    """User profile page"""
    user = User.objects.filter(email=request.user.email)  # Retrieve the user from the database. Where a user email is equal to whatever email is stored in the request object.
    return render(request, 'profile.html', {'profile': user})
