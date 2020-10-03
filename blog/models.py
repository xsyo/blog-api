from django.db import models
from django.contrib.auth import get_user_model

from .utils import img_upload_function

UserModel = get_user_model()


class Heading(models.Model):
    '''Модель рубрики'''

    name = models.CharField(max_length=100, verbose_name='Название рубрики')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Рубрика'
        verbose_name_plural = 'Рубрики'
        ordering = ['name',]

class Post(models.Model):
    '''Модель поста блога'''

    title = models.CharField(max_length=250, verbose_name='Название поста')
    img = models.ImageField(upload_to=img_upload_function, blank=True, null=True, verbose_name='Изобродение поста')
    author = models.ForeignKey(UserModel, related_name='my_posts', verbose_name='Автор поста', on_delete=models.CASCADE)
    content = models.TextField(verbose_name='Контент поста')
    published = models.DateTimeField(auto_now_add=True, verbose_name='Дата и время публикации')
    heading = models.ForeignKey(Heading, related_name='posts', on_delete=models.CASCADE, verbose_name='Рубрика поста')
    likes = models.ManyToManyField(UserModel, related_name='liked_posts', verbose_name='Лайки поста')

    @property
    def likes_count(self):
        '''Rоличество лайков у поста'''

        return self.likes.count()

    @property
    def comments_count(self):
        '''Количество комментариев у поста'''

        return self.comments.count()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        pass

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'
        ordering = ['-published',]


class Сomment(models.Model):
    '''Модель коментария'''

    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE, verbose_name='Пост к которуму принадлежит комментарий')
    author = models.ForeignKey(UserModel, related_name='my_comments', on_delete=models.CASCADE, verbose_name='Автор комментария')
    text = models.CharField(max_length=250, verbose_name='Текс комментария')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата и время написания комментария')

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
        ordering = ['-created_at',]


