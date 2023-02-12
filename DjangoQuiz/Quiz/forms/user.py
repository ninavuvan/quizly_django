from django.contrib.auth.forms import UserChangeForm

from Quiz.models.profile import Profile


class UserForm(UserChangeForm):
    class Meta:
        model = Profile
        fields = ('email', 'name', 'last_name')
