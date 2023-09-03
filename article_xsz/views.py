import datetime

import pandas

from article_xsz.models import xszst
from article_xsz.models import ys

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




        queryset = xszst.objects.filter(科目名称__contains='行政费用').exclude(科目名称__contains='研发费用').exclude(科目名称__contains='环保投入')
        df=read_frame(queryset)


        df['费用'] = df['费用'].str.extract(r'/(.*)$')
        df['费用'] = df['费用'].str.replace(r'-.*','',regex=True)
        df['费用'] = df['费用'].str.replace(r'.*宣传.*', '宣传费', regex=True)
        #df=df[(df['借方']>0)+(df['借方']<0)]
        df=df[(df['月']>=begin)*(df['月']<=end)]
        dfm=df[['年','月','凭证号','科目名称','新部门','费用','摘要','借方']].fillna(0)
        print("dfm",dfm)
        dfm=dfm.loc[(dfm['借方']!=0)].to_dict(orient='records')

        pivolt_table=df.pivot_table(
            index=['费用'],

            columns='年',

            values='借方',
            aggfunc='sum',
        )
        oder=['办公费','电话费','资料费','会务费','业务招待费','协调费','差旅费（国内）','差旅费（国外）','车辆使用费','低值易耗品摊销','聘请中介机构费','社会团体费','物业管理费','股改上市费','技术咨询（服务）费','网络信息费','诉讼费','宣传费']
        o2=[]

        for i in oder:

            if i in pivolt_table.index:
                o2.append(i)


        pivolt_table=pivolt_table.loc[o2]
        pivolt_table=pivolt_table

        pivolt_data=pivolt_table.reset_index().fillna(0)
        pivolt_data.loc['合计']=pivolt_data.sum()
        pivolt_data.loc['合计','费用']='合计'

        pivolt_data = pivolt_data.fillna(0)
       # print(pivolt_data)
        pivolt_data =pivolt_data.round(2).to_dict(orient='records')

        #print(dfm)

        return Response((pivolt_data,dfm))

class PivoltTableView_ys(APIView):
    permission_classes = [IsAdminUserOrReadOnly]
    def get(self,request):

        year=self.request.query_params.get('year')


        if year:
            year = int(year)
        else:
            year =int(datetime.datetime.today().year)
        month = self.request.query_params.get('month')
        if month:
            month = int(month)
        else:
            month = int(datetime.datetime.today().month)

        print(year,month)




        queryset = xszst.objects.filter(科目名称__contains='行政费用').exclude(科目名称__contains='研发费用').exclude(科目名称__contains='环保投入')
        queryset2 = ys.objects.all()

        df_ys=read_frame(queryset2).fillna(0)
        df_ys=df_ys[df_ys['年']==year]
        df_ys=df_ys[['费用项目','总额不含税']].set_index('费用项目')
        print(df_ys)
        df=read_frame(queryset)


        df['费用'] = df['费用'].str.extract(r'/(.*)$')
        df['费用'] = df['费用'].str.replace(r'-.*','',regex=True)
        df['费用'] = df['费用'].str.replace(r'.*宣传.*', '宣传费', regex=True)
        #df=df[(df['借方']>0)+(df['借方']<0)]
        df=df[(df['年']==year)*(df['月']<=month)]
        dfm=df[['年','月','凭证号','科目名称','新部门','费用','摘要','借方']].fillna(0)
        print("dfm",dfm)
        dfm=dfm.loc[(dfm['借方']!=0)].to_dict(orient='records')

        pivolt_table=df.pivot_table(
            index=['费用'],



            values='借方',
            aggfunc='sum',
        )
        oder=['办公费','电话费','资料费','会务费','业务招待费','协调费','差旅费（国内）','差旅费（国外）','车辆使用费','低值易耗品摊销','聘请中介机构费','社会团体费','物业管理费','股改上市费','技术咨询（服务）费','网络信息费','诉讼费','宣传费']
        o2=[]

        for i in oder:

            if i in pivolt_table.index:
                o2.append(i)


        pivolt_table=pivolt_table.loc[o2]
        pivolt_table=pivolt_table

        pivolt_data=pivolt_table.reset_index().fillna(0)
        pivolt_data.loc['合计']=pivolt_data.sum()
        pivolt_data.loc['合计','费用']='合计'

        pivolt_data = pivolt_data.fillna(0)
        pivolt_data9=pivolt_data.set_index('费用')
        df_ys = df_ys.join(other=pivolt_data9, how='left', lsuffix='', rsuffix='_R').reset_index().fillna(0)
        df_ys['进度预算']=((month/12)*df_ys['总额不含税']).round(2)
        df_ys['剩余进度预算']=df_ys['进度预算']-df_ys['借方']
        df_ys['剩余总进度预算'] = df_ys['总额不含税'] - df_ys['借方']
        df_ys=df_ys.rename(columns={"总额不含税":"全年总预算"})

        df_ys.loc['合计']=df_ys.sum()
        print(df_ys)
       # print(pivolt_data)
        pivolt_data =df_ys.round(2).to_dict(orient='records')

        #print(dfm)

        return Response((pivolt_data,dfm))

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

            queryset = xszst.objects.filter(科目名称__contains=r'专项储备\安全投入')
            df = read_frame(queryset)

            #本月
            dfby = df[(df['年'] == 2023) * (df['月'] == end)]


            #累计
            df = df[(df['月'] >= begin) * (df['月'] <= end)]
            dfn = df[df['年'] ==2023 ]
            dfn=dfn[['年','月','凭证号','科目名称','安全环保投入类型','摘要','借方']].to_dict(orient='records')
            print('安全费用明细：',dfn)
            # 累计

            pivolt_table = df.pivot_table(
                index=['安全环保投入类型'],
                columns='年',

                values='借方',
                aggfunc='sum',
            )
            #累计透视表
            col_order=['安全设施及特种设备检测检验支出','安全生产宣传、教育、培训支出','开展重大危险源和事故隐患评估、监控和整改支出','配备和更新现场作业人员安全防护用品支出','其他与安全生产直接相关的支出','完善、改造和维护安全防护设施设备支出','安全生产检查、评价、咨询和标准化建设支出','配备、维护、保养应急救援器材、设备支出和应急演练应急支出','安全生产适用的新技术、新标准、新工艺、新装备的推广、应用支出','消防救援相关支出']
            od=[]
            for i in col_order:
                if i in pivolt_table.index:
                    od.append(i)
            pivolt_table=pivolt_table.loc[od]
            pivolt_data = pivolt_table.fillna(0)
            #本月透视表
            pivolt_table_by = dfby.pivot_table(
                index=['安全环保投入类型'],


                values='借方',
                aggfunc='sum',
            )
            pivolt_data_by = pivolt_table_by.fillna(0)
            print(pivolt_data_by)

            pivolt_data=pivolt_data.join(other=pivolt_data_by,how='left',lsuffix='',rsuffix='_R').reset_index().fillna(0)
            print(pivolt_data)

            pivolt_data=pivolt_data.rename(columns={"借方":str(end)})
            pivolt_data.loc['合计'] = pivolt_data.sum()
            pivolt_data.loc['合计', '安全环保投入类型'] = '合计'



            pivolt_data = pivolt_data.round(2).to_dict(orient='records')


            return Response((pivolt_data,dfn))

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
