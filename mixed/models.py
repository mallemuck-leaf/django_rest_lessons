from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=30)


class Category(models.Model):
    category = models.CharField(max_length=20)
    info = models.TextField(max_length=1000)


class Post(models.Model):
    title = models.CharField(max_length=100)
    info = models.CharField(max_length=100)
    text = models.TextField()
    author = models.CharField(max_length=20)


class MultiLanguageContent(models.Model):
    title_ru = models.CharField(max_length=20)
    title_en = models.CharField(max_length=20)
    text_ru = models.TextField()
    text_en = models.TextField()
