from django.contrib import admin

from Quiz.models.profile import Profile
from Quiz.models.quiz import QuizQuestion, Choice, Quiz
from Quiz.models.role import Role

admin.site.register(Quiz)
admin.site.register(QuizQuestion)
admin.site.register(Choice)
admin.site.register(Profile)
admin.site.register(Role)

