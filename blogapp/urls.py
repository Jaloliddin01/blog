from django.urls import path
from .views import PostListView, AboutView

urlpatterns = [
    path("", AboutView.as_view()),
    path('blog/', PostListView.as_view()),
]