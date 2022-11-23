from django.shortcuts import render
from django.http import HttpResponse
import matrixalg
 
# Create your views here.
def index(request):
    n = request.GET.get('size')
    return HttpResponse(matrixalg.main(n), content_type='application/json')
