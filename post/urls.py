from django.urls import path
from . views import*

urlpatterns = [
    path('',homepage.as_view(), name = 'home'),
    path('detail/<int:pk>/',detail.as_view(), name = 'detail'),
    path('add/',createpost.as_view(), name='addpost'),
    path('post/update/<int:pk>/',updatepost.as_view(), name = 'update'),
    path('post/<int:pk>/remove',deletepost.as_view(), name = 'delete'),
    path("category/<str:cats>/", categoryview, name = 'category')
]