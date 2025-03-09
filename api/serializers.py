from rest_framework import serializers
from django.conf import settings
from .models import Prompt, Page


class ImageURLMixin:
    """Mixin to add image_url field to serializers."""
    image_url = serializers.SerializerMethodField()

    def get_image_url(self, obj):
        """Returns the full URL by concatenating STORAGE_ROOT_URL with the image filename."""
        if obj.image:  # `obj.image` is just the filename string
            return f"{settings.STORAGE_ROOT_URL}{obj.image}"
        return None  # No image

class PromptSerializer(ImageURLMixin, serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField()

    class Meta:
        model = Prompt
        fields = ["id", "title", "content", "image_url", "created_at"] 


class PageSerializer(ImageURLMixin, serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField()

    class Meta:
        model = Page
        fields = ["id", "title", "slug", "content", "video", "image_url", "created_at"] 
