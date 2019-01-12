from django.db import models
from django.contrib.auth.models import User


class UserInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.PROTECT, related_name='user', verbose_name='Пользователь')
    phone = models.CharField(max_length=50, verbose_name='Телефон')
    friend = models.ManyToManyField(User, blank=True, related_name='friend', verbose_name='friend')
    photo = models.ImageField(blank=True, null=True, verbose_name='Аватар')

    def __str__(self):
        return self.user.get_full_name()


class Post(models.Model):
    author = models.ForeignKey(User, related_name='article', on_delete=models.PROTECT, verbose_name='Пользователь')
    title = models.CharField(max_length=200, verbose_name='Заголовок')
    text = models.TextField(max_length=3000, verbose_name='Текст')
    date_created = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')

    def __str__(self):
        return "%s. %s (%s)" % (self.pk, self.title, self.date_created)
