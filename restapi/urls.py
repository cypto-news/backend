from django.urls import include, re_path
# from django.conf.urls import url
from rest_framework import routers
from .views import apiNews, apiMarket

# router = routers.DefaultRouter()
# router.register('newss', views.NewsViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
# urlpatterns = [
#     path('', include(router.urls)),
#     path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
# ]

urlpatterns = [ 
    # class news
    re_path(r'^news/view_news$', apiNews.view_news),
    re_path(r'^news/create_news$', apiNews.create_news), #
    re_path(r'^news/delete_all_news$', apiNews.delete_all_news),
    re_path(r'^news/detail_news/(?P<pk>[0-9]+)$', apiNews.detail_news),
    re_path(r'^news/delete_news/(?P<pk>[0-9]+)$', apiNews.delete_news),
    re_path(r'^news/update_news/(?P<pk>[0-9]+)$', apiNews.update_news),
    
    
    # class market
    re_path(r'^market/list_coin$', apiMarket.list_coin),
    re_path(r'^market/trend_market$', apiMarket.trend_market),
    re_path(r'^market/view_market$', apiMarket.view_market),
    re_path(r'^market/create_market$', apiMarket.create_market),
    re_path(r'^market/delete_market/(?P<pk>[0-9]+)$', apiMarket.delete_market),
    re_path(r'^market/update_market/(?P<pk>[0-9]+)$', apiMarket.update_market),
    
    
    
]