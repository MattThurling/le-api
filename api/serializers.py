from rest_framework import serializers
from django.conf import settings
from .models import Prompt

class PromptSerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField()

    class Meta:
        model = Prompt
        fields = ["id", "title", "content", "image_url", "created_at"]  # ✅ Expose full image URL

    def get_image_url(self, obj):
        """Returns the full URL by concatenating STORAGE_ROOT_URL with the image filename."""
        if obj.image:  # `obj.image` is just the filename string
            return f"{settings.STORAGE_ROOT_URL}{obj.image}"
        return None  # No image
