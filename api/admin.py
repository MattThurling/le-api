from django.contrib import admin
from .models import Prompt, Page

@admin.register(Prompt, Page)
class PromptAdmin(admin.ModelAdmin):
  list_display = ('title', 'created_at') 
  search_fields = ('title', 'content') 
  list_filter = ('created_at',)
  ordering = ('-created_at',)

