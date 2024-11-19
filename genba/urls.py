from django.urls import path
from genba import views

urlpatterns = [
    path('', views.home, name="home"),
    path('schedule/', views.schedule, name="schedule"),
    path('schedule_details/', views.schedule_details, name="schedule_details"),
    path('report/', views.report, name="report"),
    path('genba_list/', views.genba_list, name="genba_list"),
    path('genba_details/', views.genba_details, name="genba_details"),
    path('user_list/', views.user_list, name="user_list"),
    path('report_list/', views.report_list, name="report_list"),
    path('login_user/', views.login_user, name="login_user"),
    path('logout_user/', views.logout_user, name="logout_user"),
    path('register_user/', views.register_user, name="register_user"),
    path('add_user/', views.add_user, name="add_user"),
]
