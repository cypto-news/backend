from django.urls import include, re_path
# from django.conf.urls import url
from rest_framework import routers
from . import views

# router = routers.DefaultRouter()
# router.register('newss', views.NewsViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
# urlpatterns = [
#     path('', include(router.urls)),
#     path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
# ]

urlpatterns = [ 
    re_path(r'^api/view_news$', views.view_news),
    re_path(r'^api/create_news$', views.create_news), #
    re_path(r'^api/delete_all_news$', views.delete_all_news),
    re_path(r'^api/detail_news/(?P<pk>[0-9]+)$', views.detail_news),
    re_path(r'^api/delete_news/(?P<pk>[0-9]+)$', views.delete_news),
    re_path(r'^api/update_news/(?P<pk>[0-9]+)$', views.update_news),
]