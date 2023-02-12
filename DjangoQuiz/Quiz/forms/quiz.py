from django import forms

from Quiz.forms.choice import ChoiceFormSet
from Quiz.models.quiz import Quiz, QuizQuestion


class QuizForm(forms.ModelForm):
    class Meta:
        model = Quiz
        fields = ['title', 'description']

    questions = forms.CharField(widget=forms.Textarea(attrs={'rows': 3}))

    def save(self, commit=True):
        quiz = super().save(commit=commit)
        questions_data = self.cleaned_data.pop('questions')
        questions = [text.strip() for text in questions_data.split('\n') if text.strip()]
        for question_text in questions:
            question = QuizQuestion.objects.create(text=question_text, quiz=quiz)
            formset = ChoiceFormSet(self.data, instance=question, prefix=f'question-{question.id}-choice')
            if formset.is_valid():
                formset.save()
        return quiz
