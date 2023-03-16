from django.urls import path
from app2.views import *
app_name='my world'
urlpatterns=[
    path('mom/',mom,name='mom'),
    path('dad/',dad,name='dad'),
]