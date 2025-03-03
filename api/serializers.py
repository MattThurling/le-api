from rest_framework import serializers
from django.conf import settings
from .models import Prompt

class PromptSerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField()

    class Meta:
        model = Prompt
        fields = ["id", "title", "content", "image_url", "created_at"] 

    def get_image_url(self, obj):
        request = self.context.get("request")
        if obj.image:
            return request.build_absolute_uri(obj.image.url) if request else f"{settings.STORAGE_ROOT_URL}{obj.image.url}"
        return None
