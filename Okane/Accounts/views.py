from django.shortcuts import render
from .models import User
from django.core.exceptions import ObjectDoesNotExist, ValidationError
from rest_framework import exceptions
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import UserSerializer
from rest_framework import status
# Create your views here.




@api_view(["POST", "GET"])
def userView(request):
    """
    A util view to get all users and to create new users to test out the app
    """
    if(request.method == "GET"):
        allUsers = User.objects.all()
        serializer = UserSerializer(allUsers, many = True)
        return Response(serializer.data , status= status.HTTP_201_CREATED)


    if(request.method == "POST"):
        serializer = UserSerializer(data = request.data)
        if(serializer.is_valid()):
            serializer.save()
            return Response(serializer.data)
        
        
        return Response(serializer.errors , status= status.HTTP_400_BAD_REQUEST)




@api_view(["GET"])
def userDetailView(request, id : int):
    """
    End point to get a particular user
    """

    if(request.method == "GET"):
        try:
            user = User.objects.get(id = id)
        except ObjectDoesNotExist:
            raise exceptions.ValidationError("User with id = {} does not exist".format(id))

        serializer = UserSerializer(instance= user)

        return Response(serializer.data)



@api_view(["GET"])
def userSearch(request, email : str):
    """
    End point to get a particular user, using the email id, registered
    """

    if(request.method == "GET"):
        try:
            user = User.objects.get(email = email)
        except ObjectDoesNotExist:
            raise exceptions.ValidationError("User with email = {} does not exist".format(email))

        serializer = UserSerializer(instance= user)

        return Response(serializer.data)