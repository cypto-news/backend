from rest_framework import serializers

from .models import News


class NewsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        db_table = 'news' # KALO DB ERROR GANTI INI JADI "restapi_news"
        model = News
        fields = ('id','title', 'description', 'date', 'urlImg')