from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import Prompt, Page, Post
from .serializers import PromptSerializer, PageSerializer, PostSerializer

@api_view(['GET'])
def prompts_list(request):
  prompts = Prompt.objects.all()
  serializer = PromptSerializer(prompts, many=True)
  return Response(serializer.data)

@api_view(['GET'])
def pages_list(request):
  pages = Page.objects.all()
  serializer = PageSerializer(pages, many=True)
  return Response(serializer.data)

@api_view(['GET'])
def page_by_slug(request, slug):
    page = get_object_or_404(Page, slug=slug)
    serializer = PageSerializer(page)
    return Response(serializer.data)

@api_view(['GET'])
def posts_list(request):
  posts = Post.objects.all()
  serializer = PostSerializer(posts, many=True)
  return Response(serializer.data)

@api_view(['GET'])
def post_by_slug(request, slug):
    post = get_object_or_404(Post, slug=slug)
    serializer = PostSerializer(post)
    return Response(serializer.data)

