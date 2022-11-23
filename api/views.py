from django.views import View
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import ArrayDiagonale
from .serializers import ArrayDiagonaleSerializers
import matrixalg

# Create your views here.
class ArrayDiagonaleView(APIView):
        
        def get(self, request):
                size = request.GET.get('size')
                a = matrixalg.main(size)
                result = ArrayDiagonale(a['массив'], a['диагональ'])

                serializer_for_request = ArrayDiagonaleSerializers(instance=result)

                return Response(serializer_for_request.data)