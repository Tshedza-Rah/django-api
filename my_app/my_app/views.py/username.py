from djago.shortcuts import render
from django.http import HttpRequest

#creat your views here.


@api_view(['GET'])
def user_name(requests):
    return Response({"message": "Asak Manoo"})
    

