from django.shortcuts import render
from .models import BlogPost, Category
from rest_framework import generics
from .serializers import BlogPostSerializer, CategorySerializer

'''Views: Blog'''

# GET All Blog Posts
class BlogPostList(generics.ListAPIView):
    # API to list blog posts.
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer

# GET Single Blog Post
class BlogPostDetail(generics.RetrieveAPIView):
    # Check for a single Blog Post.
    # API endpoint that returns a single blog post by pk.
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer

# POST Blog Post
class BlogPostCreate(generics.CreateAPIView):
    # API to create blog post.
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer

# UPDATE Blog Post
class BlogPostUpdate(generics.RetrieveUpdateAPIView):
    # API to update blog post.
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer

# DELETE Blog Post
class BlogPostDelete(generics.RetrieveDestroyAPIView):
    # API to delete blog post.
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer


'''Views: Category'''

# GET All Categories
class CategoryList(generics.ListAPIView):
    # API to list categories.
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

# GET Single Category Post
class CategoryDetail(generics.RetrieveAPIView):
    # Check for a single Category Post.
    # API endpoint that returns a single category by pk.
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

# POST Category Post
class CategoryCreate(generics.CreateAPIView):
    # API to create category.
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

# UPDATE Category Post
class CategoryUpdate(generics.RetrieveUpdateAPIView):
    # API to update category.
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

# DELETE Category Post
class CategoryDelete(generics.RetrieveDestroyAPIView):
    # API to delete category.
    queryset = Category.objects.all()
    serializer_class = CategorySerializer