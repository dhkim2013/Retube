# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from rest_framework import generics
from rest_framework.response import Response

from service.models import Playlist
from service.serializers import PlaylistSerializer


class Index(View):
    def get(self, request):
        if request.user.is_authenticated:
            username = request.user.username
            return render(request, 'service/index_for_user.html', {'username': username})
        return render(request, 'service/index.html')

class PlaylistListCreateView(generics.ListCreateAPIView):
    queryset = Playlist.objects.all()
    serializer_class = PlaylistSerializer
    filter_fields = ('owner__username',)

class PlaylistRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Playlist.objects.all()
    serializer_class = PlaylistSerializer