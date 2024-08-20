from django.contrib.auth.models import User, Group
from django.views.generic.edit import CreateView
from django.contrib.auth.views import LoginView, LogoutView
from .models import BaseRegisterForm
from django.shortcuts import redirect
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required

class BaseRegisterView(CreateView):
    model = User
    form_class = BaseRegisterForm
    success_url = '/'

@login_required
def AddToAuthorsGroup(request): #добавление пользователя в группу с правами автора
    if not request.user.groups.filter(name='authors').exists():
        authors_group=Group.objects.get(name='authors')
        user=request.user
        authors_group.user_set.add(user)
    return redirect('main_page')
