from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from django.utils import timezone
from Login.models import *

class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    writer = models.ForeignKey(Writer, verbose_name="Yazar", on_delete=models.CASCADE, related_name='posts', null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)
    content = RichTextField()
    is_published = models.BooleanField(default=False)
    live_date = models.DateTimeField(default=timezone.now)    
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    is_delete = models.BooleanField(verbose_name=('Silindi?'), default=False)
    delete_date = models.DateTimeField(verbose_name=('Silinme Tarihi'), blank=True, null=True) 

    def save(self, *args, **kwargs):
        if not self.writer_id:
            # Varsayılan yazarı burada belirleyin veya geçici olarak bir yazar belirleyin
            default_writer = Writer.objects.first()  # veya başka bir yazar seçme yöntemi
            self.writer = default_writer
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

class Like(models.Model):
    post = models.ForeignKey(Post, verbose_name=('Post'), on_delete=models.CASCADE, related_name='likes')
    user = models.ForeignKey(User, verbose_name=('Kullanıcı'), on_delete=models.CASCADE)
    create_date = models.DateTimeField(verbose_name=('Oluşturma Tarihi'), default=timezone.now)    
    update_date = models.DateTimeField(verbose_name=('Son güncelleme tarihi'), auto_now=True)
    is_delete = models.BooleanField(verbose_name=('Silindi?'), default=False)
    delete_date = models.DateTimeField(verbose_name=('Silinme Tarihi'), blank=True, null=True)

    class Meta:
        verbose_name = 'Beğeni'
        verbose_name_plural = 'Beğeniler'
        ordering = ['-create_date']

    def __str__(self):
        if self.user.first_name and self.user.last_name:
            return f"{self.user.first_name} {self.user.last_name} - {self.post.title}"
        else:
            return f"{self.user.username} - {self.post.title}"

class Dislike(models.Model):
    post = models.ForeignKey(Post, verbose_name=('Post'), on_delete=models.CASCADE, related_name='dislikes')
    user = models.ForeignKey(User, verbose_name=('Kullanıcı'), on_delete=models.CASCADE)
    create_date = models.DateTimeField(verbose_name=('Oluşturma Tarihi'), default=timezone.now)
    update_date = models.DateTimeField(verbose_name=('Son güncelleme tarihi'), auto_now=True)
    is_delete = models.BooleanField(verbose_name=('Silindi?'), default=False)
    delete_date = models.DateTimeField(verbose_name=('Silinme Tarihi'), blank=True, null=True)

    class Meta:
        verbose_name = 'Beğenmeme'
        verbose_name_plural = 'Beğenmemeler'
        ordering = ['-create_date']

    def __str__(self):
        if self.user.first_name and self.user.last_name:
            return f"{self.user.first_name} {self.user.last_name} - {self.post.title}"
        else:
            return f"{self.user.username} - {self.post.title}"
        

class Comment(models.Model):
    post = models.ForeignKey(Post, verbose_name=("Post"), on_delete=models.CASCADE, related_name='comments')
    content = models.CharField(verbose_name=("Yorum"), max_length=512)
    user = models.ForeignKey(User, verbose_name=("Kullanıcı"), on_delete=models.CASCADE)
    create_date = models.DateTimeField(verbose_name=('Oluşturma Tarihi'), default=timezone.now)
    update = models.DateTimeField(verbose_name=("Son Güncelleme Tarihi"), auto_now_add=True)
    is_delete = models.BooleanField(verbose_name=('Silindi?'), default=False)
    delete_date = models.DateTimeField(verbose_name=("Silinme Tarihi"), blank=True, null=True)

    class Meta:
        verbose_name = 'Yorum'
        verbose_name_plural = 'Yorumlar'
        ordering = ['-create_date']

    def __str__(self):
        if self.user.first_name and self.user.last_name:
            return f"{self.user.first_name} {self.user.last_name} - {self.content[:50]}"
        else:
            return f"{self.user.username} - {self.content[:50]}"
        