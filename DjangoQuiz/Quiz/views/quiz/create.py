from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

from Quiz.forms.quiz import QuizForm
from Quiz.models.quiz import Quiz


class QuizCreateView(CreateView):
    model = Quiz
    form_class = QuizForm
    success_url = reverse_lazy('quiz_list')
    template_name = 'quiz_create.html'
