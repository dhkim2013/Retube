from django.conf.urls import url

from service import views

urlpatterns = [
    url(r'$^', views.Index.as_view()),
]