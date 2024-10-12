from django.shortcuts import render, get_object_or_404
from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticatedOrReadOnly
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, GenericAPIView
from .models import Product, Category, Post, MultiLanguageContent
from .serializers import User, UserSerializer
from .serializers import ProductSerializer, CategorySerializer, PostSerializer
from .serializers import MultiLanguageContentWriteSerializer, RuMultiLanguageContentReadSerializer, EnMultiLanguageContentReadSerializer
from . import mixins as u_mixins


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class ProductListCreateView(APIView):

    def get(self, request, pk=None):
        if pk is not None:
            product = get_object_or_404(Product, pk=pk)
            serializer = ProductSerializer(product)
            return Response(serializer.data)
        else:
            products = Product.objects.all()
            serializer = ProductSerializer(products, many=True)
            return Response(serializer.data)

    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
@permission_classes([AllowAny])
def category_view(request, pk=None):
    if request.method == 'GET':
        if pk is not None:
            category = Category.object.get(pk=pk)
            serializer = CategorySerializer(category)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            categories = Category.objects.all()
            serializer = CategorySerializer(categories, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PostListCreateView(u_mixins.CreatedByMixin, ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    # permission_classes = [IsAuthenticatedOrReadOnly]


class PostDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class MultiLanguageContentListCreateView(u_mixins.CreatedByMixin, ModelViewSet):
    queryset = MultiLanguageContent.objects.all()
