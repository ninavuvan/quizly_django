from django.contrib.auth.views import PasswordChangeView
from django.shortcuts import render
from django.urls import reverse_lazy

from Quiz.forms.password_changing import PasswordsChangingForm


class PasswordsChangeView(PasswordChangeView):
    form_class = PasswordsChangingForm
    success_url = reverse_lazy('password_success')


def password_success(request):
    return render(request, 'registration/password_success.html', {})
