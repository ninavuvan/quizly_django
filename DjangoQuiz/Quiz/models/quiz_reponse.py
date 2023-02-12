from django.db import models
from django.contrib.auth import get_user_model
from Quiz.models.quiz import QuizQuestion, Quiz

User = get_user_model()


class QuizResponse(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(QuizQuestion, on_delete=models.CASCADE)
    answer = models.ForeignKey('Choice', on_delete=models.CASCADE)
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user} answered {self.answer} to {self.question} in {self.quiz}'

    def get_score(self):
        correct_answers = 0
        questions = self.quiz.get_questions()
        for question in questions:
            if self.is_question_correct(question):
                correct_answers += 1
        return (correct_answers / len(questions)) * 100

    def is_question_correct(self, question):
        selected_choice = self.answer
        return selected_choice.is_correct and selected_choice.question == question
