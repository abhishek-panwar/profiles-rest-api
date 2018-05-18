from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.

class HelloApiView(APIView):
    """Test API View """

    def get(self, rewuest, format=None):
        """returns a list of APIView features"""
        an_apiview = [
            'Uses HTTP methods as function (get, post, put, patch, delete)',
            'its similar to traditional django view',
            'gives you most control over your logic',
            'is mapped manually to URLs'
        ]

        return Response({'message': 'Hello!', 'an_apiview': an_apiview})
