from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET'])
def get_message(request):
    return Response({"message": "Hello from Django!"}, content_type="application/json")
