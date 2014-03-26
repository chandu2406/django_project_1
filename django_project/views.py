from django.contrib.auth import logout
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.contrib.auth.views import login
from registration.backends.default.views import RegistrationView
from registration.forms import RegistrationFormUniqueEmail

def main_page(request):
    return render_to_response('index.html')


def custom_login(request, **kwargs):
    if request.user.is_authenticated():
        return HttpResponseRedirect('/gs/')
    else:
        return login(request)


def logout_page(request):
    """
    Log users out and re-direct them to the main page.
    """
    logout(request)
    return HttpResponseRedirect('/')

class RegistrationViewUniqueEmail(RegistrationView):
    form_class = RegistrationFormUniqueEmail