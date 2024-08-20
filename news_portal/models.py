from random import randint as rint

from django.db import models
from django.core.validators import MinValueValidator
from django.contrib.auth.models import User
from datetime import datetime



class Author(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    raiting=models.IntegerField(default=0)
    state=False

    def __str__(self):
        return self.user.username

    def update_rating(self): #обновление рейтинга автора по трем критериям

        # Расчет рейтинга постов автора
        _raiting=Post.objects.filter(author_id=self.id).values('raiting')
        post_raiting=0
        for pst in _raiting:
            post_raiting +=pst['raiting']
        post_raiting *=3 # утроенное значение суммы рейтингов постов

        # Расчет рейтинга комментов автора
        _raiting = Comment.objects.filter(user_id=self.user.id).values('raiting')
        comm_raiting=0
        for cmt in _raiting:
            comm_raiting +=cmt['raiting']

        # Расчет суммы рейтингов комментов к статьям автора
        _raiting = Comment.objects.filter(post__author=self).values('raiting')
        comm_posts_raiting=0
        for cmt_pst in _raiting:
            comm_posts_raiting +=cmt_pst['raiting']

        self.raiting=post_raiting+comm_raiting+comm_posts_raiting
        self.save()

class Category(models.Model):
    category=models.CharField(max_length=100, unique=True) # тематика поста
    subscribers=models.ManyToManyField(User, through='UserSubcribes')

    def __str__(self):
        return self.category

class Post(models.Model):
    news = 'NS'
    article = 'AL'
    post_type = [(news, 'Новости'),  # список названий типа поста
                 (article, 'Статья')]

    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True)
    postType = models.CharField(choices=post_type, default=news, max_length=2) # тип поста (новость/статья)
    create_time = models.DateTimeField(auto_now_add=True)  # дата добавления поста
    category=models.ManyToManyField(Category, through='PostCategory')
    title=models.CharField(max_length=100) #заголовок поста
    content=models.TextField(blank=True) # содержание поста
    raiting=models.IntegerField(default=0) # рейтинг поста

    def __str__(self):
        return f'{self.content[:30:]}, {self.author.user.username} '

    def set_date(self, y_): # функция изменения даты публикации в БД
                            # через shell сугубо для учеьных целей
        h, m, s =rint(0,24),rint(0,59),rint(0,59)
        m_,d_=rint(1,12), rint(1,28)
        self.create_time=datetime(y_,m_,d_,h,m,s)
        self.save()

    # Увеличение и уменьшение рейтинга поста
    def like(self):
        self.raiting += 1
        self.save()
    def dislike(self):
        self.raiting -= 1
        self.save()

    def get_id(self):
        return self.pk

    def preview(self): # предварительный просмотр статьи
        return f'{self.content[:124:]}......'

class PostCategory(models.Model):
    post=models.ForeignKey(Post, on_delete=models.CASCADE)
    category=models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.category.category

class Comment(models.Model):
    post=models.ForeignKey(Post, on_delete=models.CASCADE)
    user=models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    comment_text=models.CharField(max_length=200)
    create_time = models.DateTimeField(auto_now_add=True)
    raiting=models.IntegerField(default=0)

    # Увеличение и уменьшение рейтинга комментариев
    def like(self):
        self.raiting += 1
        self.save()
    def dislike(self):
        self.raiting -= 1
        self.save()

class Mail(models.Model): # модель для работы с почтой
    date=models.DateField(default=datetime.utcnow())
    client=models.CharField(max_length=200)
    message=models.TextField()

    def __str__(self):
        return f'{self.client} : {self.message}'

class UserSubcribes (models.Model): # класс, определяющий на какие категории публикаци подписаны пользователи
    subcribe=models.ForeignKey(User, on_delete=models.DO_NOTHING)
    category=models.ForeignKey(Category, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.subcribe.email


# Create your models here.
