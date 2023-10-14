from django.urls import path
from .views import *


urlpatterns=[
    path('', Home, name='Home'),
    path('Collect_noun_and_verb', Collect_noun_and_verb, name='Collect_noun_and_verb'),

]