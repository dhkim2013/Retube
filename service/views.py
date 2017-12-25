# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.views import View
from rest_framework import generics

from service.models import Playlist
from service.serializers import PlaylistSerializer


class Index(View):
    def get(self, request):
        if request.user.is_authenticated:
            return render(request, 'service/index_for_user.html')
        return render(request, 'service/index.html')

class PlaylistListCreateView(generics.ListCreateAPIView):
    queryset = Playlist.objects.all()
    serializer_class = PlaylistSerializer

class PlaylistRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Playlist.objects.all()
    serializer_class = PlaylistSerializer