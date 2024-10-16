from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Product, Category, Post, MultiLanguageContent


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'is_active']


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'


class RuMultiLanguageContentReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = MultiLanguageContent
        fields = ['title_ru', 'text_ru']


class EnMultiLanguageContentReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = MultiLanguageContent
        fields = ['title_en', 'text_en']


class MultiLanguageContentWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = MultiLanguageContent
        fields = '__all__'
