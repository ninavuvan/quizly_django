from django.forms import forms

from Quiz.models.quiz import QuizQuestion


class QuestionForm(forms.ModelForm):
    class Meta:
        model = QuizQuestion
        fields = ['text']
