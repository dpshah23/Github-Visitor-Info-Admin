from django.urls import path
from .views import *

urlpatterns = [
    path('login/',login,name='login'),
    path('logout/',logout,name='logout'),
    path('validate/',validate,name='validate'),
    path('register/',signup,name='signup'),
    path('signup/',signup,name='signup'),
]
