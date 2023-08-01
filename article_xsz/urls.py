from django.urls import path
from article_xsz import views
#
app_name = 'article_xsz_pivolt'
#
urlpatterns = [
    path('', views.PivoltTableView.as_view(), name='list'),
    path('aqfy/', views.PivoltTableView_aqfy.as_view(), name='list2'),
    path('ys/', views.PivoltTableView_ys.as_view(), name='list3'),
    #path('<int:pk>/', views.PivoltTableView.as_view(), name='detail'),
]