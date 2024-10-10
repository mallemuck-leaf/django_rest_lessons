from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Product(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Rating(models.Model):
    product = models.ForeignKey('Product', on_delete=models.CASCADE, related_name='product_rating')
    rating = models.IntegerField(default=5,
                                 validators=[MinValueValidator(0), MaxValueValidator(10)])

    def __str__(self):
        return str(self.rating)


class Comment(models.Model):
    product = models.ForeignKey('Product', on_delete=models.CASCADE, related_name='product_comment')
    comment = models.TextField()

    def __str__(self):
        return self.comment[:20]
