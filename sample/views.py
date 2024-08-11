from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET'])
def sample(request):
    return Response({"message": "This is a sample response"})
