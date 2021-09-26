from rest_framework import response
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.serializers import Serializer
from .models import Writetext
from .serializers import WritetextSerializer

# Create your views here.
@api_view(['GET'])
def helloAPI(request):
    return Response("Hello world~!!!!!")

@api_view(['GET'])
def WriteTextList(request):
    totalWriteText = Writetext.objects.all()

    Serializer = WritetextSerializer(totalWriteText, many=True)
    return Response(Serializer.data)