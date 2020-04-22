from rest_framework import viewsets, mixins
from MyUsers.serializers import UserSerializer
from MyUsers.models import UserProfile

class UserViewSet(mixins.ListModelMixin,
                     mixins.RetrieveModelMixin,
                     mixins.UpdateModelMixin,
                     mixins.DestroyModelMixin,
                     mixins.CreateModelMixin,
                     viewsets.GenericViewSet):

    queryset = UserProfile.objects.all()
    serializer_class = UserSerializer

# from rest_framework.views import APIView
# from MyUsers.serializers import UserSerializer
# from .models import UserProfile
# from rest_framework.response import Response
#
#
# class UserListView(APIView):
#     '''
#     商品列表
#     '''
#     def get(self,request,format=None):
#         users = UserProfile.objects.all()
#         users_serialzer = UserSerializer(users,many=True)
#         return Response(users_serialzer.data)