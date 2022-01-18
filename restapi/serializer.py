from rest_framework import serializers

from .models import News, Market


class NewsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        db_table = 'news' # KALO DB ERROR GANTI INI JADI "restapi_news"
        model = News
        fields = ('id','title', 'description', "source", "rhn",'date', 'urlImg')
        
class MarketSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        db_table = 'market'
        model = Market
        fields = ('id', 'coin', 'date', 'price', 'logo_coin')