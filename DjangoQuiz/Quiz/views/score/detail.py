from django.views.generic.detail import DetailView

from Quiz.models.quiz_reponse import QuizResponse


class ScoreDetailView(DetailView):
    model = QuizResponse
    template_name = 'score_detail.html'
    context_object_name = 'quiz_response'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        quiz_response = self.object
        context['quiz'] = quiz_response.quiz
        context['correct_answers'] = quiz_response.get_score()
        return context
