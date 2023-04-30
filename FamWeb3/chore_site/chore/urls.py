from django.urls import path
from . import views

app_name = 'chore'

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('user_login/',views.user_login, name='user_login'),
    path('timesheet/',views.submit_timesheet, name='timesheet'),
    path('loan_application/',views.loan_application, name='loan')
]