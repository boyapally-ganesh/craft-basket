from django.urls import path
from . import views



urlpatterns = [
    path('register/',views.userregisterview, name='register'),
    path('login/',views.login_form, name = 'login'),
    path('logout/',views.user_logout, name = 'logout'),
    path('edit/',views.user_profile, name = 'edituser'),
   # path('edit/',views.change_passwordwithout, name ='edituser'),
]