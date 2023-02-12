from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView


class LoginView(LoginView):
    template_name = 'login.html'


class LogoutView(LoginRequiredMixin, LogoutView):
    template_name = 'logout.html'
