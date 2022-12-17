from rest_framework.decorators import api_view
from rest_framework.response import Response
from store.models import Store
# from store.serializers import storeListSerializer
from rest_framework.views import APIView
from django.http import Http404
# from store.serializers import storeDetailSerializer
from rest_framework import status
from rest_framework import mixins
from rest_framework import generics
# from rest_framework.permissions import IsAdminUser
from store.permissions import IsAdminUserOrReadOnly
from rest_framework import viewsets
from store.serializers import StoreSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from store.models import Category
from store.serializers import CategorySerializer, CategoryDetailSerializer
from store.models import Tag
from store.serializers import TagSerializer
from store.serializers import StoreDetailSerializer

from store.models import Avatar
from store.serializers import AvatarSerializer


class AvatarViewSet(viewsets.ModelViewSet):
    queryset = Avatar.objects.all()
    serializer_class = AvatarSerializer
    permission_classes = [IsAdminUserOrReadOnly]


class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = [IsAdminUserOrReadOnly]
    pagination_class = None


class CategoryViewSet(viewsets.ModelViewSet):
    """分类视图集"""
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAdminUserOrReadOnly]
    pagination_class = None

    def get_serializer_class(self):
        if self.action == 'list':
            return CategorySerializer
        else:
            return CategoryDetailSerializer


class StoreViewSet(viewsets.ModelViewSet):
    """博文视图集"""
    queryset = Store.objects.all()
    serializer_class = StoreSerializer
    permission_classes = [IsAdminUserOrReadOnly]

    filter_backends = [filters.SearchFilter]
    search_fields = ['title']

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def get_serializer_class(self):
        if self.action == 'list':
            return StoreSerializer
        else:
            return StoreDetailSerializer

    # filterset_fields = ['author__username', 'title']

    # def get_queryset(self):
    #     queryset = self.queryset
    #     username = self.request.query_params.get('username', None)
    #
    #     if username is not None:
    #         queryset = queryset.filter(author__username=username)
    #
    #     return queryset

# class storeDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = store.objects.all()
#     serializer_class = storeDetailSerializer
#     permission_classes = [IsAdminUserOrReadOnly]
#
#
# class storeList(generics.ListCreateAPIView):
#     queryset = store.objects.all()
#     serializer_class = storeListSerializer
#     permission_classes = [IsAdminUserOrReadOnly]
#
#     def perform_create(self, serializer):
#         serializer.save(author=self.request.user)

# @api_view(['GET', 'POST'])
# def store_list(request):
#     if request.method == 'GET':
#         stores = store.objects.all()
#         serializer = storeListSerializer(stores, many=True)
#         return Response(serializer.data)
#
#     elif request.method == 'POST':
#         serializer = storeListSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class storeDetail(APIView):
#     """文章详情视图"""
#
#     def get_object(self, pk):
#         """获取单个文章对象"""
#         try:
#             return store.objects.get(pk=pk)
#         except:
#             raise Http404
#
#     def get(self, request, pk):
#         store = self.get_object(pk)
#         serializer = storeDetailSerializer(store)
#         return Response(serializer.data)
#
#     def put(self, request, pk):
#         store = self.get_object(pk)
#         serializer = storeDetailSerializer(store, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def delete(self, request, pk):
#         store = self.get_object(pk)
#         store.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


# class storeDetail(mixins.RetrieveModelMixin,
#                     mixins.UpdateModelMixin,
#                     mixins.DestroyModelMixin,
#                     generics.GenericAPIView):
#     """文章详情视图"""
#     queryset = store.objects.all()
#     serializer_class = storeDetailSerializer
#
#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)
#
#     def put(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)
#
#     def delete(self, request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs)
