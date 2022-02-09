# a = {
#     "data":[
#         {
#             "coin" : "ETH",
#             "date" : "2022-01-13",
#             "price": 3366.28,
#             "logo_coin": "https://www.logo.wine/a/logo/Ethereum/Ethereum-Icon-Purple-Logo.wine.svg"
#         },
#         {
#             "coin" : "ETH",
#             "date" : "2022-01-12",
#             "price": 3364.11,
#             "logo_coin": "https://www.logo.wine/a/logo/Ethereum/Ethereum-Icon-Purple-Logo.wine.svg"
#         }
#     ]
# }

# print(a["data"][0])


#     def view_market(request):
#         if request.method == 'GET':
#             market = Market.objects.all().order_by('date')
#             coin = request.GET.get('coin', None)
#             if coin is not None:
#                 market = market.filter(title__icontains=coin)
#             market_serializer = MarketSerializer(market, many=True)
#             return JsonResponse(market_serializer.data, safe=False)
#         else:
#             return JsonResponse(status=status.HTTP_400_BAD_REQUEST)
        
#     def view_news(request):
#         if request.method == 'GET':
#             news = News.objects.all().order_by('date')
#             title = request.GET.get('title', None)
#             if title is not None:
#                 news = news.filter(title__icontains=title)
#             news_serializer = NewsSerializer(news, many=True)
#             return JsonResponse(news_serializer.data, safe=False)
#         else:
#             return JsonResponse(status=status.HTTP_400_BAD_REQUEST)