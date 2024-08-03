from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('get_week_data/', get_week_data, name='get_week_data'),
]
