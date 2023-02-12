from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView

from Quiz.models.quiz import Quiz


class QuizListView(LoginRequiredMixin, ListView):
    model = Quiz
    template_name = 'quiz_list.html'
    context_object_name = 'quizzes'
