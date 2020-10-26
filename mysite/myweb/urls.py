from django.contrib import admin
from django.urls import path, include
from myweb.views import RegisterUserView
from myweb.views import LoginView
from myweb.views import LogoutView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('myweb.urls')),
    path('registeration/', RegisterUserView, name='register_user'),
    path('login/', LoginView, name='login'),
    path('logout/', LogoutView, name='logout'),
]