from django.urls import path
from genba import views

urlpatterns = [
    path('<int:year>/<int:month>/<int:day>', views.home, name="home"),
    path('login_user/', views.login_user, name="login"),
    path('logout_user/', views.logout_user, name="logout"),
    path('register_user/', views.register_user, name="register"),
]
