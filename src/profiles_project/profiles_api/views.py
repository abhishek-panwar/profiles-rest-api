from django.shortcuts import render

from rest_framework import viewsets

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import TokenAuthentication


from . import serializers
from . import models
from . import permissions


# Create your views here.

class HelloApiView(APIView):
    """Test API View """

    serializer_class = serializers.HelloSerializer



    def get(self, request, format=None):
        """returns a list of APIView features"""
        an_apiview = [
            'Uses HTTP methods as function (get, post, put, patch, delete)',
            'its similar to traditional django view',
            'gives you most control over your logic',
            'is mapped manually to URLs'
        ]

        return Response({'message': 'Hello!', 'an_apiview': an_apiview})

    def post(self, request):
        """create a hello message with our name"""

        serializer = serializers.HelloSerializer(data=request.data)

        if serializer.is_valid():
            name = serializer.data.get('name')
            message = 'Hello {0}'.format(name)
            return Response({'message': message})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        """handles updating an object"""

        return Response({'method': 'put'})


    def patch(self, request, pk=None):
        """patch request, only update fields provided in the request"""

        return Response({'method': 'patch'})

    def delete(self, request, pk=None):
        """deletes an object"""

        return Response({'method': 'delete'})
        #return Response('han bhai')


class HelloViewSet(viewsets.ViewSet):
    """test API Viewset"""

    serializer_class = serializers.HelloSerializer

    def create(self, request):
        """creates a new hello message"""
        serializer = serializers.HelloSerializer(data=request.data)
        if serializer.is_valid():
            name = serializer.data.get('name')
            message = 'Hello {0}'.format(name)
            return Response({'message':message})

        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)


    def retrieve(self, request, pk=None):
        """handles getting an object by its ID"""
        return Response({'http_method': 'GET'})

    def update(self, request, pk=None):
        """updates an object"""
        return Response({'http_method': 'PUT'})

    def partial_update(self, request, pk=None):
        """updates part of an object"""
        return Response({'http_method': 'PATCH'})

    def destroy(self, request, pk=None):
        """removes an object"""
        return Response({'http_method': 'DELETE'})



    def list(self, request):
        """return a hello message"""

        a_viewset = [
        'uses actions (list, create, retrieve, update, partial_upadte)',
        'Automatically maps to URLs using Routers',
        'Provides more functionality with less code'
        ]

        return Response({'message': 'Hello!', 'a_viewset': a_viewset})


class UserProfileViewSet(viewsets.ModelViewSet):
    """handles creatinf, reading and updating profiles"""

    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()

    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
    








            #
