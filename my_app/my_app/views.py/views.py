from djago.shortcuts import render
from django.http import HttpRequest

#creat your views here.


@api_view(['GET'])
def hello_world(requests):
    return Response({"message": "Hello, world!"})

