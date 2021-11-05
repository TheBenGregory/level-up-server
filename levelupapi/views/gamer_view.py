from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from levelupapi.models import Gamer


class GamerView(ViewSet):
    

    def retrieve(self, request, pk=None):
       
        try:
            gamer = Gamer.objects.get(pk=pk)
            serializer = GamerSerializer(gamer, context={'request': request})
            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)

    def list(self, request):
       
        gamers = Gamer.objects.all()

        
        serializer = GamerSerializer(
            gamers, many=True, context={'request': request})
        return Response(serializer.data)

class GamerSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Gamer
        fields = ('id', 'user', 'bio')