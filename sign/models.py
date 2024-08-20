from allauth.account.forms import SignupForm
from allauth.socialaccount.forms import SignupForm as SocialSignupForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User, Group
from django import forms
#
class BaseRegisterForm(UserCreationForm):
    email = forms.EmailField(label = "Email")
    first_name = forms.CharField(label = "First name")
    last_name = forms.CharField(label = "Last name")

    def save(self, *args, **kwargs):
        user = super(BaseRegisterForm, self).save(*args, **kwargs)
        common_group = Group.objects.get(name="common")
        common_group.user_set.add(user)
        return user

    class Meta:
        model = User
        fields = ("username",
                  "first_name",
                  "last_name",
                  "email",
                  "password1",
                  "password2", )

class CommonSignupForm(SignupForm):
    def save(self, request):
        user=super(CommonSignupForm,self).save(request)
        common_group=Group.objects.get(name="common")
        common_group.user_set.add(user)
        return user

class SocialCommonSignupForm(SocialSignupForm):
    def save(self, request):
        user=super(SocialCommonSignupForm,self).save(request)
        common_group=Group.objects.get(name="common")
        common_group.user_set.add(user)
        return user