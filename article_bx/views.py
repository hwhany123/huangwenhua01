from django.shortcuts import render
from article_bx.models import bx_clbx

from article_bx.permissions import IsAdminUserOrReadOnly
from rest_framework import viewsets
from article_bx.serializers import ArticleSerializer

from rest_framework import filters



from article_bx.serializers import ArticleDetailSerializer








class ArticleViewSet(viewsets.ModelViewSet):
    """博文视图集"""
    queryset = bx_clbx.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = [IsAdminUserOrReadOnly]

    filter_backends = [filters.SearchFilter]
    search_fields = ['报销人']

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def get_serializer_class(self):
        if self.action == 'list':
            return ArticleSerializer
        else:
            return ArticleDetailSerializer

# Create your views here.
