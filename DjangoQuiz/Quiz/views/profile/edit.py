from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import UpdateView

from Quiz.forms.user import UserForm
from Quiz.models.profile import Profile


class ProfileEditView(LoginRequiredMixin, UpdateView):
    model = Profile
    form_class = UserForm
    template_name = 'profile_edit.html'
    success_url = reverse_lazy('profile')

    def get_object(self, queryset=None):
        return self.request.user
