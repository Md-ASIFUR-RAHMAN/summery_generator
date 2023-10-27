from django.urls import path
from .views import Collect_noun_and_verb,Home,SentenceAnalysisView



urlpatterns=[
    path('', Home, name='Home'),
    path('Collect_noun_and_verb', Collect_noun_and_verb, name='Collect_noun_and_verb'),
    path('noun_&_verb/v1/API', SentenceAnalysisView.as_view(), name='noun_&_verb'),

]