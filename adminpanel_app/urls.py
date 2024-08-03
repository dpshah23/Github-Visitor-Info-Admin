from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('get_week_data/', get_week_data, name='get_week_data'),
    path('get_link/',get_link,name='get_link'),
    path('get_specific_day/',get_specific_day,name='get_specific_day')
]
