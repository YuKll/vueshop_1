# from rest_framework import serializers
#
#
# class GoodsSerializer(serializers.Serializer):
#     name = serializers.CharField(required=True,max_length=100)
#     click_num = serializers.IntegerField(default=0)
#     goods_front_image = serializers.ImageField()

from rest_framework import serializers, viewsets
from goods.models import Goods, GoodsCategory

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = GoodsCategory
        fields = "__all__"

class GoodsSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    class Meta:
        #url = serializers.HyperlinkedIdentityField(view_name="myLesson-detail")
        model = Goods
        fields = "__all__"