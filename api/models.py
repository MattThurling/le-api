from django.db import models

class Prompt(models.Model):
  title = models.CharField(max_length=255)
  content = models.TextField()
  image = models.CharField(max_length=255)
  created_at = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return self.title

class Page(models.Model):
  title = models.CharField(max_length=255)
  slug = models.SlugField(unique=True)
  content = models.TextField()
  image = models.CharField(max_length=255, null=True, blank=True)
  video = models.CharField(max_length=255, null=True, blank=True)
  created_at = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return self.title

class Post(models.Model):
  title = models.CharField(max_length=255)
  slug = models.SlugField(unique=True)
  content = models.TextField()
  image = models.CharField(max_length=255, null=True, blank=True)
  video = models.CharField(max_length=255, null=True, blank=True)
  created_at = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return self.title