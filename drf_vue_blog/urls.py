"""drf_vue_blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from rest_framework.routers import DefaultRouter
from article import views
from article_xsz import views as views_xsz
from article_bx import views as views_bx
from store import views as views_store
from comment.views import CommentViewSet

from django.conf import settings
from django.conf.urls.static import static

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from user_info.views import UserViewSet

router = DefaultRouter()
router.register(r'article', views.ArticleViewSet)
router.register(r'article_xsz', views_xsz.ArticleViewSet)
#router.register(r'article_pivolt',views_xsz.PivoltTableView)
router.register(r'article_bx', views_bx.ArticleViewSet)
router.register(r'store', views_store.StoreViewSet)
router.register(r'category', views.CategoryViewSet)
router.register(r'store_category', views_store.CategoryViewSet)
router.register(r'tag', views.TagViewSet)
router.register(r'store_tag', views_store.TagViewSet)
router.register(r'avatar', views.AvatarViewSet)
router.register(r'store_avatar', views_store.AvatarViewSet)
router.register(r'comment', CommentViewSet)
router.register(r'user', UserViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    # 可视化接口
    path("api-auth/", include("rest_framework.urls")),
    # drf 默认路由器自动注册
    path("api/", include(router.urls)),
    path("api/article_xsz_pivolt/", include("article_xsz.urls",namespace="article_xsz_pivolt")),

    path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),

    # article
    # path('api/article/', include('article.urls', namespace='article')),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
