from django.urls import path
from .views import LessonView, ExerciseView

urlpatterns = [
    path('lessons/', LessonView.as_view()),
    path('exercises/', ExerciseView.as_view()),
]