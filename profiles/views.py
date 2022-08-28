from django.contrib.auth.views import LoginView
from django.views.generic import CreateView

from vacancy.forms import MyAuthenticationForm, SignUpForm


class UserSignupView(CreateView):
    form_class = SignUpForm
    success_url = '/login'
    template_name = 'profiles/register.html'


class UserLoginView(LoginView):
    authentication_form = MyAuthenticationForm
    redirect_authenticated_user = True
    template_name = 'profiles/login.html'
