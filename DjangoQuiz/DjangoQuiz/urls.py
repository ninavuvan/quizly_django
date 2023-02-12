"""DjangoQuiz URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Quiz.views import *
from Quiz.views.home import HomeView
from Quiz.views.login import LoginView, LogoutView
from Quiz.views.password_change import PasswordsChangeView
from Quiz.views.profile.edit import ProfileEditView
from Quiz.views.profile.profile import ProfileView
from Quiz.views.quiz.create import QuizCreateView
from Quiz.views.quiz.detail import QuizDetailView
from Quiz.views.quiz.list import QuizListView
from Quiz.views.register import RegisterView
from Quiz.views.score.detail import ScoreDetailView
from Quiz.views.score.list import ScoreListView

urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('', HomeView.as_view(), name='home'),
    path('accounts/login/', LoginView.as_view(), name='login'),
    path('accounts/logout/', LogoutView.as_view(), name='logout'),
    path('accounts/register/', RegisterView.as_view(), name='register'),
    path('accounts/profile/', ProfileView.as_view(), name='profile'),
    path('accounts/profile/edit', ProfileEditView.as_view(), name='edit_profile'),
    path('quiz/list', QuizListView.as_view(), name='quiz_list'),
    path('quiz/detail/<int:pk>', QuizDetailView.as_view(), name='quiz_detail'),
    path('score/list', ScoreListView.as_view(), name='score_list'),
    path('score/detail/<int:pk>', ScoreDetailView.as_view(), name='score_detail'),
    path('quiz/create/', QuizCreateView.as_view(), name='quiz_create'),
    path('accounts/profile/edit/password/', PasswordsChangeView.as_view(), name='edit_password'),
]
