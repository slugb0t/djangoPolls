# file used to call views from out polls web app
from django.urls import path
from . import views

urlpatterns = [
    # ex: polls/
    path('', views.IndexView.as_view(), name="index"),
    path('<int:question_id>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]