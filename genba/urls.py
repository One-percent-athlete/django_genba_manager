from django.urls import path
from genba import views

urlpatterns = [
    path('', views.home, name="home"),
    path('schedule/', views.schedule, name="schedule"),
    path('report/', views.report, name="report"),
    path('genba_list/', views.genba_list, name="genba_list"),
    path('user_list/', views.user_list, name="user_list"),
    path('<int:year>/<int:month>/<int:day>/', views.dashboard, name="dashboard"),
    path('login_user/', views.login_user, name="login"),
    path('logout_user/', views.logout_user, name="logout"),
    path('register_user/', views.register_user, name="register"),
]
