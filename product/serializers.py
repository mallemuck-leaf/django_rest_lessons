from rest_framework import serializers
from .models import MinValueValidator, MaxValueValidator, Product, Rating, Comment


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'


class DataProductSerializer(serializers.ModelSerializer):
    # ratings = RatingSerializer(many=True)

    class Meta:
        model = Product
        depth = 1
        fields = ['id', 'name', 'product_rating', 'product_comment']
    # product = serializers.CharField(max_length=30)
    # rating = serializers.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(10)])
    # comments = serializers.ListField()
