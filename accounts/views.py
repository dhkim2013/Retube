# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import os
from django.conf import settings
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render

# Create your views here.
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.core.files import File


@method_decorator(csrf_exempt, name='dispatch')
class LoginView(View):
    def get(self, request):
        logout(request)
        return render(request, 'accounts/login.html')

    def post(self, request):
        logout(request)
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)

        if user is None:
            return JsonResponse({'success': 'false', 'error': 'user', 'message': '존재하지 않는 사용자입니다.'})
        else:
            login(request, user)
            return JsonResponse({'success': 'true', 'message': '로그인 성공'})

@method_decorator(csrf_exempt, name='dispatch')
class RegisterView(View):
    def get(self, request):
        logout(request)
        return render(request, 'accounts/register.html')

    def post(self, request):
        logout(request)
        username = request.POST.get('username')
        password = request.POST.get('password')
        firstName = request.POST.get('firstName')
        print('first name : {}'.format(firstName))

        try:
            User.objects.get(username=username)
            return JsonResponse({'success': 'false', 'error': 'username', 'message': '이미 존재하는 이메일입니다.'})
        except:
            User.objects.create_user(username=username, password=password, first_name=firstName)
            return JsonResponse({'success': 'true', 'message': '성공적으로 만들어졌습니다.'})

class LogoutView(View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect('/')