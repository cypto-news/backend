# from rest_framework import viewsets
# from django.shortcuts import render
import datetime
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from urllib.parse import quote, urlencode, urljoin, urlsplit
 
# from .models import News
# from .serializer import NewsSerializer
from rest_framework.decorators import api_view

from .serializer import NewsSerializer, MarketSerializer
from .models import News, Market, Predict


# class NewsViewSet(viewsets.ModelViewSet):
#     queryset = News.objects.all().order_by('date')
#     serializer_class = NewsSerializer


class apiNews:
## GET API REQUEST
    def view_news(request):
        if request.method == 'GET':
            news = News.objects.all().order_by('date')
            title = request.GET.get('title', None)
            if title is not None:
                news = news.filter(title__icontains=title)
            
            news_serializer = NewsSerializer(news, many=True)
            return JsonResponse(news_serializer.data, safe=False)
        else:
            return JsonResponse(status=status.HTTP_400_BAD_REQUEST)
    
    def detail_news(request, pk):
        if request.method == 'GET':
            news = News.objects.get(pk=pk)
            news_serializer = NewsSerializer(news) 
            return JsonResponse(news_serializer.data)
            
    ## POST API REQUEST
    @csrf_exempt
    def create_news(request):
        if request.method == 'POST':
            news_data = JSONParser().parse(request)
            news_data = NewsSerializer(data=news_data)
            if news_data.is_valid():
                news_data.save()
                return JsonResponse(news_data.data, status=status.HTTP_201_CREATED) 
            return JsonResponse(news_data.errors, status=status.HTTP_400_BAD_REQUEST)
    
    # DELETE API REQUEST
    @csrf_exempt
    def delete_news(request, pk):
        if request.method == 'DELETE': 
            news = News.objects.get(pk=pk) # find news by pk (id) 
            news.delete() 
            return JsonResponse({'message': 'news was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT) 

    @csrf_exempt
    def delete_all_news(request):
        if request.method == 'DELETE':
            count = News.objects.all().delete()
            return JsonResponse({'message': '{} news were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)
        
            
    # UPDATE API REQUEST
    @csrf_exempt
    def update_news(request,pk):
        if request.method == 'PUT': 
            news = News.objects.get(pk=pk)
            news_data = JSONParser().parse(request) 
            news_serializer = NewsSerializer(news, data=news_data) 
            if news_serializer.is_valid(): 
                news_serializer.save() 
                return JsonResponse(news_serializer.data) 
            return JsonResponse(news_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
        pass


class apiMarket:
    def view_market(request):
        if request.method == 'GET':
            market = Market.objects.all().order_by('date')
            coin = request.GET.get('coin', None)
            if coin is not None:
                market = market.filter(coin__icontains=coin)
            market_serializer = MarketSerializer(market, many=True)
            return JsonResponse(market_serializer.data, safe=False)
        else:
            return JsonResponse(status=status.HTTP_400_BAD_REQUEST)
        
    def trend_market(request):
        if request.method == 'GET':
            market = Market.objects.filter(date__gte=datetime.date(2022, 1,17))
            market_serializer = MarketSerializer(market, many=True)
            return JsonResponse(market_serializer.data, safe=False)
        else:
            return JsonResponse(status=status.HTTP_400_BAD_REQUEST)
    
    def list_coin(request):
        if request.method == 'GET':
            lcoin = Market.objects.order_by('coin').values_list('coin', flat=True).distinct()
            lcoin = list(lcoin)
            return JsonResponse(lcoin, safe=False)
        else:
            return JsonResponse(status=status.HTTP_400_BAD_REQUEST)
        
    @csrf_exempt
    def create_market(request):
        if request.method == 'POST':
            market_data = JSONParser().parse(request)
            for i in market_data["data"]:
                data = MarketSerializer(data=i)
                if data.is_valid():
                    data.save()
            return JsonResponse({'message': 'list market was created successfully!'}, status=status.HTTP_201_CREATED) 
            # return JsonResponse(market_data.errors, status=status.HTTP_400_BAD_REQUEST)
        
    @csrf_exempt
    def delete_market(request, pk):
        if request.method == 'DELETE': 
            market = Market.objects.get(pk=pk) # find news by pk (id) 
            market.delete() 
            return JsonResponse({'message': 'news was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT) 
        
    @csrf_exempt
    def update_market(request,pk):
        if request.method == 'PUT': 
            market = Market.objects.get(pk=pk)
            market_data = JSONParser().parse(request) 
            market_serializer = MarketSerializer(market, data=market_data) 
            if market_serializer.is_valid(): 
                market_serializer.save() 
                return JsonResponse(market_serializer.data) 
            return JsonResponse(market_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
        pass
        
    
        