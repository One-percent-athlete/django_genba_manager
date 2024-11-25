from django.urls import path
from genba import views

urlpatterns = [
    path('', views.home, name="home"),
    path('schedule/', views.schedule, name="schedule"),
    path('schedule_details/', views.schedule_details, name="schedule_details"),
    path('report_list/', views.report_list, name="report_list"),
    path('report_details/', views.report_details, name="report_details"),
    path('add_report/', views.add_report, name="add_report"),
    # path('add_genba', views.add_genba, name="add_genba"),
    path('genba_list/', views.genba_list, name="genba_list"),
    path('genba_details/', views.genba_details, name="genba_details"),
    path('user_list/', views.user_list, name="user_list"),
    path('login_user/', views.login_user, name="login_user"),
    path('logout_user/', views.logout_user, name="logout_user"),
    path('add_user/', views.add_user, name="add_user"),
]
