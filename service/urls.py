from django.conf.urls import url

from service import views

urlpatterns = [
    url(r'^$', views.Index.as_view()),
    url(r'^playlist/$', views.PlaylistListCreateView.as_view()),
    url(r'^playlist/(?P<pk>[0-9]+)/$', views.PlaylistRetrieveUpdateDestroyView.as_view()),
]