from django.urls import path
from .views import prompts_list, pages_list, page_by_slug

urlpatterns = [
  path('prompts/', prompts_list),
  path('pages/', pages_list),
  path('pages/<slug:slug>/', page_by_slug, name='page-by-slug'),
]
