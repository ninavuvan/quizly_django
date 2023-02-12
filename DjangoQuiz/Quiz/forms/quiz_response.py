from django import forms

from Quiz.models.quiz import Choice
from Quiz.models.quiz_reponse import QuizResponse


class QuizResponseForm(forms.ModelForm):
    choice = forms.ModelChoiceField(queryset=Choice.objects.none(),
                                    widget=forms.RadioSelect,
                                    empty_label=None)

    class Meta:
        model = QuizResponse
        fields = ('choice',)

    def __init__(self, *args, **kwargs):
        questions = kwargs.pop('questions')
        super().__init__(*args, **kwargs)
        for question in questions:
            self.fields[f'question{question.id}'] = forms.ModelChoiceField(
                queryset=question.choice_set.all(),
                widget=forms.RadioSelect,
                empty_label=None
            )

    def save(self, commit=True, *args, **kwargs):
        quiz_response = super().save(commit=False, *args, **kwargs)
        if commit:
            quiz_response.save()
        return quiz_response
