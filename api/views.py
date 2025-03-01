from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Prompt
from .serializers import PromptSerializer

@api_view(['GET'])
def prompts_list(request):
  prompts = Prompt.objects.all()
  serializer = PromptSerializer(prompts, many=True)
  return Response(serializer.data)

