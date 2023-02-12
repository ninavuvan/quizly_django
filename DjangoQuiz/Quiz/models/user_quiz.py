from django.db import models

from Quiz.models.profile import Profile
from Quiz.models.quiz import Quiz


class UserQuiz(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    score = models.FloatField()
    date_taken = models.DateTimeField(auto_now_add=True)
