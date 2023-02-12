from django.forms import inlineformset_factory
from django import forms

from Quiz.models.quiz import Choice, QuizQuestion


class ChoiceForm(forms.ModelForm):
    is_correct = forms.BooleanField(required=False)

    class Meta:
        model = Choice
        fields = ['text', 'is_correct']


ChoiceFormSet = inlineformset_factory(QuizQuestion, Choice, form=ChoiceForm, extra=1)
