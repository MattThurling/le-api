from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import Prompt, Page
from .serializers import PromptSerializer, PageSerializer

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

