import datetime

from django import forms
from .models import Post, Author, Category
from django.core.exceptions import ValidationError
from datetime import datetime

class PostForm(forms.Form):
    author = forms.ModelChoiceField(label='Автор', queryset=Author.objects.all())
    postType=forms.ChoiceField(label='Тип публикации',choices=Post.post_type)
    create_time = forms.DateTimeField  (label='Дата создания публикации', required=False, disabled=True)
    title = forms.CharField(label='Заголовок публикации', max_length=50)
    content= forms.CharField(label='Содержание публикации', widget=forms.Textarea)
    category = forms.ModelMultipleChoiceField(queryset=Category.objects.all(), widget=forms.CheckboxSelectMultiple)

    def clean(self): # проверка не слишком ли короткое название
        check=super().clean()
        title=check.get('title')
        if len(title)<5:
            raise ValidationError({'title':'Слишком короткое название.'})
        return check

class SubsribeForm(forms.Form): # форма для подписок на категории публикаций
    category = forms.ModelMultipleChoiceField(queryset=Category.objects.all(), disabled=True,
                      widget=forms.CheckboxSelectMultiple, label='Подписки пользователя')