from django.urls import path
from .views import ProductListCreateView, RatingListCreateView, CommentListCreateView, DataProductView

urlpatterns = [
    path('product/', ProductListCreateView.as_view()),
    path('rating/', RatingListCreateView.as_view()),
    path('comment/', CommentListCreateView.as_view()),
    path('product_data/', DataProductView.as_view()),
]
