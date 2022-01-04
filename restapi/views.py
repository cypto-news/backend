# from rest_framework import viewsets
# from django.shortcuts import render

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
from django.views.decorators.csrf import csrf_exempt
from urllib.parse import quote, urlencode, urljoin, urlsplit
 
# from .models import News
# from .serializer import NewsSerializer
from rest_framework.decorators import api_view

from .serializer import NewsSerializer
from .models import News


# class NewsViewSet(viewsets.ModelViewSet):
#     queryset = News.objects.all().order_by('date')
#     serializer_class = NewsSerializer

## GET API REQUEST
def view_news(request):
    if request.method == 'GET':
        news = News.objects.all()
        print(news)
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
def delete_news(request, pk):
    if request.method == 'DELETE': 
        news = News.objects.get(pk=pk) # find news by pk (id) 
        news.delete() 
        return JsonResponse({'message': 'news was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT) 
    
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