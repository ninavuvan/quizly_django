from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Count
from django.views.generic import ListView

from Quiz.models.quiz import Quiz


class ScoreListView(LoginRequiredMixin, ListView):
    model = Quiz
    template_name = 'score_list.html'

    def get_queryset(self):
        return super().get_queryset().annotate(
            num_responses=Count('quizresponse')
        ).order_by('-num_responses')