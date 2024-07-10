from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField  # Using ckeditor.fields for Rich Text Editor
from django.utils.text import slugify

class Reader(models.Model):
    user = models.ForeignKey(User, verbose_name="Kullanıcı", on_delete=models.SET_NULL, null=True)
    phone = models.CharField(max_length=20, null=True, blank=True)
    is_darkmode = models.BooleanField(verbose_name="Dark Mode", default=False)
    created_date = models.DateTimeField(verbose_name="Oluşturma Tarihi", auto_now_add=True)
    updated_date = models.DateTimeField(verbose_name="Son Güncelleme Tarihi", auto_now=True)

    is_delete = models.BooleanField(verbose_name="Silindi", default=False)
    delete_date = models.DateTimeField(verbose_name="Silinme Tarihi", blank=True, null=True)
    slug = models.SlugField(verbose_name="Url", unique=True)

    def __str__(self):
        if self.user.first_name and self.user.last_name:
            return f"{self.user.first_name} {self.user.last_name}"
        else:
            return self.user.username
        
    def save(self, *args, **kwargs):
        if not self.slug:
            full_name = f"{self.user.first_name} {self.user.last_name}".replace('ı', 'i')
            proposed_slug = slugify(full_name)
            if Reader.objects.filter(slug=proposed_slug).exists():
                counter = 1
                while True:
                    new_slug = f"{proposed_slug}-{counter}"
                    if not Reader.objects.filter(slug=new_slug).exists():
                        proposed_slug = new_slug
                        break
                    counter += 1
            self.slug = proposed_slug
        super().save(*args, **kwargs)

class Writer(models.Model):
    user = models.ForeignKey(User, verbose_name="Kullanıcı", on_delete=models.SET_NULL, null=True, related_name= 'writers')
    phone = models.CharField(max_length=20, null=True, blank=True)
    is_darkmode = models.BooleanField(verbose_name="Dark Mode", default=False)
    is_delete = models.BooleanField(verbose_name="Silindi", default=False)
    delete_date = models.DateTimeField(verbose_name="Silinme Tarihi", blank=True, null=True)
    created_date = models.DateTimeField(verbose_name="Oluşturma Tarihi", auto_now_add=True)
    updated_date = models.DateTimeField(verbose_name="Son Güncelleme Tarihi", auto_now=True)
    slug = models.SlugField(verbose_name="Url", unique=True, editable=False)
    bio = models.TextField(verbose_name=("Biyografi"), blank=True, null=True)

    def __str__(self):
        if self.user.first_name and self.user.last_name:
            return f"{self.user.first_name} {self.user.last_name}"
        else:
            return self.user.username
        
    def save(self, *args, **kwargs):
        if not self.slug:
            full_name = f"{self.user.first_name} {self.user.last_name}"
            proposed_slug = slugify(full_name)
            if Writer.objects.filter(slug=proposed_slug).exists():
                counter = 1
                while True:
                    new_slug = f"{proposed_slug}-{counter}"
                    if not Writer.objects.filter(slug=new_slug).exists():
                        proposed_slug = new_slug
                        break
                    counter += 1
            self.slug = proposed_slug
        super().save(*args, **kwargs)

class Article(models.Model):
    title = models.CharField(verbose_name="Başlık", max_length=100)
    content = RichTextField(verbose_name="İçerik")
    writer = models.ForeignKey(Writer, verbose_name="Yazar", on_delete=models.CASCADE)
    created_date = models.DateTimeField(verbose_name="Oluşturma Tarihi", auto_now_add=True)
    updated_date = models.DateTimeField(verbose_name="Son Güncelleme Tarihi", auto_now=True)
    is_delete = models.BooleanField(verbose_name="Silindi", default=False)
    delete_date = models.DateTimeField(verbose_name="Silinme Tarihi", blank=True, null=True)
    slug = models.SlugField(verbose_name="Url", unique=True, editable=False)

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        if not self.slug:
            proposed_slug = slugify(self.title)
            if Article.objects.filter(slug=proposed_slug).exists():
                counter = 1
                while True:
                    new_slug = f"{proposed_slug}-{counter}"
                    if not Article.objects.filter(slug=new_slug).exists():
                        proposed_slug = new_slug
                        break
                    counter += 1
            self.slug = proposed_slug
        super().save(*args, **kwargs)

class ArticleComment(models.Model):
    article = models.ForeignKey(Article, verbose_name="Makale", on_delete=models.CASCADE, related_name='comments')
    reader = models.ForeignKey(Reader, verbose_name="Okuyucu", on_delete=models.SET_NULL, null=True)
    content = models.TextField(verbose_name="Yorum")
    created_date = models.DateTimeField(verbose_name="Oluşturma Tarihi", auto_now_add=True)
    is_delete = models.BooleanField(verbose_name="Silindi", default=False)
    delete_date = models.DateTimeField(verbose_name="Silinme Tarihi", blank=True, null=True)

    def __str__(self):
        return f"{self.reader.user.username} - {self.article.title}"

class UserLog(models.Model):
    user = models.ForeignKey(User, verbose_name="Kullanıcı", on_delete=models.SET_NULL, null=True)
    action = models.CharField(verbose_name="İşlem", max_length=1024)
    created_date = models.DateTimeField(verbose_name="Oluşturma Tarihi", auto_now_add=True)

    def __str__(self):
        if self.user.first_name and self.user.last_name:
            return f"{self.user.first_name} {self.user.last_name} Logları"
        else:
            return f"{self.user.username} Logları"
