from django.urls import path
from .views import prompts_list, pages_list

urlpatterns = [
  path('prompts/', prompts_list),
  path('pages/', pages_list),
]
