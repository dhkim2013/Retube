from django.conf.urls import url

from accounts import views

urlpatterns = [
    url(r'^login/$', views.LoginView.as_view()),
    url(r'^register/$', views.RegisterView.as_view()),
    url(r'^logout/$', views.LogoutView.as_view()),
]