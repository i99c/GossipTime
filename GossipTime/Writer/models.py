from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)
    content = RichTextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    is_delete = models.BooleanField(verbose_name=('Silindi?'), default=False)
    delete_date = models.DateTimeField(verbose_name=('Silinme Tarihi'), blank=True, null=True) 

    def __str__(self):
        return self.title


class Like(models.Model):
    post = models.ForeignKey(Post, verbose_name=('Post'), on_delete=models.CASCADE, related_name='likes')
    user = models.ForeignKey(User, verbose_name=('Kullanıcı'), on_delete=models.CASCADE)
    create_date = models.DateTimeField(verbose_name=('Oluşturma Tarihi'), auto_now_add=True)
    update_date = models.DateTimeField(verbose_name=('Son güncelleme tarihi'), auto_now=True)
    is_delete = models.BooleanField(verbose_name=('Silindi?'), default=False)
    delete_date = models.DateTimeField(verbose_name=('Silinme Tarihi'), blank=True, null=True) 

    class Meta:
        verbose_name = 'Beğeni'
        verbose_name_plural = 'Beğeniler'
        ordering = ['-created-date']

    def __str__(self):
        if self.user.first_name and self.user.last_name:
            return f"{self.user.first_name} {self.user.last_name} - {self.blog.title}"
        else:
            return f"{self.user.username} - {self.blog.title}"

class Dislike(models.Model):
    post = models.ForeignKey(Post, verbose_name=('Post'), on_delete=models.CASCADE, related_name='dislikes')
    user = models.ForeignKey(User, verbose_name=('Kullanıcı'), on_delete=models.CASCADE)
    create_date = models.DateTimeField(verbose_name=('Oluşturma Tarihi'), auto_now_add=True)
    update_date = models.DateTimeField(verbose_name=('Son güncelleme tarihi'), auto_now=True)
    is_delete = models.BooleanField(verbose_name=('Silindi?'), default=False)
    delete_date = models.DateTimeField(verbose_name=('Silinme Tarihi'), blank=True, null=True) 

    class Meta:
        verbose_name = 'Beğenmeme'
        verbose_name_plural = 'Beğenmemeler'
        ordering = ['-created-date']

    def __str__(self):
        if self.user.first_name and self.user.last_name:
            return f"{self.user.first_name} {self.user.last_name} - {self.blog.title}"
        else:
            return f"{self.user.username} - {self.blog.title}"
