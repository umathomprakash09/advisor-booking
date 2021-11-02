from django.contrib import admin
from django.urls import path,include
from .views import *

urlpatterns = [
    path('user/<int:user_id>/advisor',getAdvisors),
    path('admin/advisor',addAdvisor),
    path('user/register',RegisterUser.as_view()),
    path('user/<int:user_id>/advisor/<int:advisor_id>',BookAdvisor.as_view()),
    path('user/<int:user_id>/advisor/booking',GetBookedCalls.as_view())
]