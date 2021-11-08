from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from levelupapi.models import EventGamer, Gamer


class EventGamerView(ViewSet):
    

    def retrieve(self, request, pk=None):
       
        try:
            event_gamer = EventGamer.objects.get(pk=pk)
            serializer = EventGamerSerializer(Eventgamer, context={'request': request})
            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)

    def list(self, request):
       
        event_gamers = EventGamer.objects.all()

        
        serializer = EventGamerSerializer(
            event_gamers, many=True, context={'request': request})
        return Response(serializer.data)

class GamerSerialization(serializers.ModelSerializer)

    class Meta:
        model: Gamer
        fields: ('id', )

class EventGamerSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = EventGamer
        fields = ('id', 'user', 'bio')
