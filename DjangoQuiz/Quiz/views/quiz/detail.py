from django.shortcuts import get_object_or_404, redirect
from django.views.generic import DetailView

from Quiz.models.quiz import Quiz, QuizQuestion, Choice
from Quiz.models.quiz_reponse import QuizResponse


class QuizDetailView(DetailView):
    template_name = 'quiz_detail.html'
    model = Quiz
    context_object_name = 'quiz'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        questions = QuizQuestion.objects.filter(quiz=self.object)
        context['questions'] = questions
        context['object'] = self.object
        return context

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        print(obj)
        return obj

    def post(self, request, *args, **kwargs):
        quiz = self.get_object()
        questions = quiz.quizquestion_set.all()
        user = self.request.user
        for question in questions:
            choice_id = request.POST.get(f'question{question.id}', None)
            if choice_id is not None:
                choice = get_object_or_404(Choice, id=choice_id)
                QuizResponse.objects.create(quiz=quiz, user=user, question=question, answer=choice)
        return redirect('score_detail', pk=quiz.id)
