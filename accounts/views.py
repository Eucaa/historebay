from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required  # This will stop people who aren't logged in from accessing the page.
# from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.template.context_processors import csrf
from .forms import UserLoginForm, UserRegistrationForm
# Create your views here.


def index(request):
    #  Return the index.html file (also see line 18 & 22 in urls.py)
    return render(request, 'index.html')  # Only add 'index.html' here and stick with 'index' below.


@login_required  # This decorator will check to see if the user is logged in before executing any more of the code.
def logout(request):
    #  Log user out
    auth.logout(request)
    messages.success(request, 'You have successfully been logged out!')
    return redirect(reverse('index'))


def login(request):
    """Return a login page"""
    if request.user.is_authenticated:  # This if statement prevents people form accessing the login page by entering the URL into the URL bar.
        return redirect(reverse('index'))
    if request.method == 'POST':
        login_form = UserLoginForm(request.POST)  # Create an instance of the user login form and pass it in the request.post as an other constructor so
                                                  # a new login form will be created with the data posted from the form on the UI.
        if login_form.is_valid():
            user = auth.authenticate(username=request.POST['username'],
                                     password=request.POST['password'])

            if user:
                auth.login(user, request)
                messages.success(request, "You have succesfully logged in.")

                if request.GET and request.GET['next'] != '':
                    next = request.GET['next']
                    return HttpResponseRedirect(next)
                else:
                    return redirect(reverse('index'))  # This will redirect the user to a specific other page just so that they're not redirected back to the login page again when logged in.

            else:
                login_form.add_error(None, "Username is incorrect")
    else:
        login_form = UserLoginForm()  # Otherwise, create an empty login.

    args = {'login_form': login_form, 'next': request.GET.get('next', '')}
    return render(request, 'login.html', args)


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

        if registration_form.is_valid():
            registration_form.save()  # Because the model (user=) is already specified inside of the meta class in the registration form (forms.py) it's not needed to specify model again here.

            user = auth.authenticate(username=request.POST.get['username'],
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
    user = User.objects.get(email=request.user.email)  # Retrieve the user from the database. Where a user email is equal to whatever email is stored in the request object.
    return render(request, 'profile.html', {'profile': user})