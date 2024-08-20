from django.urls import path, include
# Импортируем созданное нами представление
from .views import (PostsList, PostDetail, PostFilterView, create_post, edit_post,
                    delete_post, MailView, test)


urlpatterns = [
        path('', PostsList.as_view(),name='main_page'),
        path('edit_subscribe/', PostsList.as_view(),name='edit_subscribe'),
        path('<int:pk>/',PostDetail.as_view()),
        path('search/', PostFilterView.as_view(), name='search_post'),
        path('create/', create_post,name='create_post'),
        path('<int:pk>/edit/',edit_post, name='edit_post'),
        path('<int:pk>/delete/', delete_post, name='delete_post'),
        path('mail/', MailView.as_view(), name='news_mail'),


        # тестовый URL для апробирования разных задач
        path('test/', test, name='test')
                      ]