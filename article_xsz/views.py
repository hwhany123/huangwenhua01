import datetime

from article_xsz.models import xszst

from article_xsz.permissions import IsAdminUserOrReadOnly
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response

from article_xsz.serializers import ArticleSerializer
from django_pandas.io import read_frame
from rest_framework import filters



from article_xsz.serializers import ArticleDetailSerializer








class ArticleViewSet(viewsets.ModelViewSet):
    """博文视图集"""
    queryset = xszst.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = [IsAdminUserOrReadOnly]

    filter_backends = [filters.SearchFilter]
    search_fields = ['摘要']

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def get_serializer_class(self):
        if self.action == 'list':
            return ArticleSerializer
        else:
            return ArticleDetailSerializer

class PivoltTableView(APIView):
    permission_classes = [IsAdminUserOrReadOnly]
    def get(self,request):

        begin=self.request.query_params.get('begin')
        print(begin)

        if begin:
            begin = int(begin)
        else:
            begin =int(1)
        end = self.request.query_params.get('end')
        if end:
            end = int(end)
        else:
            end = int(datetime.datetime.today().month)

        print(begin,end)




        queryset = xszst.objects.filter(科目名称__contains='行政费用').exclude(科目名称__contains='研发支出')
        df=read_frame(queryset)

        df['费用'] = df['费用'].str.extract(r'/(.*)$')
        df['费用'] = df['费用'].str.replace(r'-.*','',regex=True)
        #df=df[(df['借方']>0)+(df['借方']<0)]
        df=df[(df['月']>=begin)*(df['月']<=end)]
        pivolt_table=df.pivot_table(
            index=['费用'],
            columns='年',

            values='借方',
            aggfunc='sum',
        )
        pivolt_data=pivolt_table.reset_index().fillna(0)




        pivolt_data =pivolt_data.to_dict(orient='records')

        return Response(pivolt_data)

class PivoltTableView_aqfy(APIView):
        permission_classes = [IsAdminUserOrReadOnly]
        def get(self, request):

            begin = self.request.query_params.get('begin')
            print(begin)

            if begin:
                begin = int(begin)
            else:
                begin = int(1)
            end = self.request.query_params.get('end')
            if end:
                end = int(end)
            else:
                end = int(datetime.datetime.today().month)

            print(begin, end)

            queryset = xszst.objects.filter(科目名称__contains='专项储备')
            df = read_frame(queryset)

            #本月
            dfby = df[(df['年'] == 2023) * (df['月'] == end)]


            #累计
            df = df[(df['月'] >= begin) * (df['月'] <= end)]
            pivolt_table = df.pivot_table(
                index=['安全环保投入类型'],
                columns='年',

                values='借方',
                aggfunc='sum',
            )
            #累计透视表
            pivolt_data = pivolt_table.reset_index().fillna(0)
            #本月透视表
            pivolt_table_by = dfby.pivot_table(
                index=['安全环保投入类型'],


                values='借方',
                aggfunc='sum',
            )
            pivolt_data_by = pivolt_table_by.reset_index().fillna(0)
            print(pivolt_data_by)

            pivolt_data=pivolt_data.join(other=pivolt_data_by,how='left',lsuffix='',rsuffix='_R').fillna(0)
            print(pivolt_data)

            pivolt_data=pivolt_data.rename(columns={"借方":str(end)}).drop('安全环保投入类型_R',axis=1)


            pivolt_data = pivolt_data.to_dict(orient='records')

            return Response(pivolt_data)

    # filterset_fields = ['author__username', 'title']

    # def get_queryset(self):
    #     queryset = self.queryset
    #     username = self.request.query_params.get('username', None)
    #
    #     if username is not None:
    #         queryset = queryset.filter(author__username=username)
    #
    #     return queryset

# class ArticleDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Article.objects.all()
#     serializer_class = ArticleDetailSerializer
#     permission_classes = [IsAdminUserOrReadOnly]
#
#
# class ArticleList(generics.ListCreateAPIView):
#     queryset = Article.objects.all()
#     serializer_class = ArticleListSerializer
#     permission_classes = [IsAdminUserOrReadOnly]
#
#     def perform_create(self, serializer):
#         serializer.save(author=self.request.user)

# @api_view(['GET', 'POST'])
# def article_list(request):
#     if request.method == 'GET':
#         articles = Article.objects.all()
#         serializer = ArticleListSerializer(articles, many=True)
#         return Response(serializer.data)
#
#     elif request.method == 'POST':
#         serializer = ArticleListSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class ArticleDetail(APIView):
#     """文章详情视图"""
#
#     def get_object(self, pk):
#         """获取单个文章对象"""
#         try:
#             return Article.objects.get(pk=pk)
#         except:
#             raise Http404
#
#     def get(self, request, pk):
#         article = self.get_object(pk)
#         serializer = ArticleDetailSerializer(article)
#         return Response(serializer.data)
#
#     def put(self, request, pk):
#         article = self.get_object(pk)
#         serializer = ArticleDetailSerializer(article, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def delete(self, request, pk):
#         article = self.get_object(pk)
#         article.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


# class ArticleDetail(mixins.RetrieveModelMixin,
#                     mixins.UpdateModelMixin,
#                     mixins.DestroyModelMixin,
#                     generics.GenericAPIView):
#     """文章详情视图"""
#     queryset = Article.objects.all()
#     serializer_class = ArticleDetailSerializer
#
#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)
#
#     def put(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)
#
#     def delete(self, request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs)
