from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, ProductListCreateView, category_view
from .views import PostListCreateView, PostDetailView, MultiLanguageContentListCreateView

router = DefaultRouter()
router.register(r'users', UserViewSet, basename='user')
router.register(r'languagecontent', MultiLanguageContentListCreateView, basename='lang')

urlpatterns = [
    path('', include(router.urls)),
    path('products/', ProductListCreateView.as_view()),
    path('products/<int:pk>', ProductListCreateView.as_view()),
    path('categories/', category_view),
    path('categories/<int:pk>', category_view),
    path('posts/', PostListCreateView.as_view()),
    path('posts/<int:pk>', PostDetailView.as_view()),
    # path('languagecontent/', MultiLanguageContentListCreateView.as_view()),
]
