from django.urls import path
from app1.views import *
app_name='love'
urlpatterns=[
    path('vinod/',vinod,name='vinod'),
    path('teju/',teju,name='teju'),
]