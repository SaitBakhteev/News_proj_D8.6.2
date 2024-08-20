from django.urls import path
from django.urls import reverse
from django.contrib.auth.views import LoginView, LogoutView
from .views import BaseRegisterView, AddToAuthorsGroup


# по причине наличия allauth адреса приложения 'sign' 'login' и 'signup'
# явдяются бесполезными. И поэтому для них условно применен шаблон index.html
urlpatterns = [
    path('login/',  #бесполезный url
         LoginView.as_view(template_name='sign/login.html'), name='login'),
    path('logout/',
         LogoutView.as_view(template_name='sign/logout.html'),name='logout'),
    path('signup/',  # бесполезный url
         BaseRegisterView.as_view(template_name ='sign/signup.html'), name='signup'),
    path('add_to_authors/', AddToAuthorsGroup, name='add_to_authors'),
]