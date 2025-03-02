from django.contrib import admin
from .models import Prompt

@admin.register(Prompt)
class PromptAdmin(admin.ModelAdmin):
  list_display = ('title', 'created_at') 
  search_fields = ('title', 'content') 
  list_filter = ('created_at',)
  ordering = ('-created_at',)

