from django.urls import path
from .views import prompts_list

urlpatterns = [
  path('prompts/', prompts_list),
]
