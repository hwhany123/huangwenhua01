from django.urls import path
from article_xsz import views
#
app_name = 'article_xsz_pivolt'
#
urlpatterns = [
    path('/', views.PivoltTableView.as_view(), name='list'),
    #path('<int:pk>/', views.PivoltTableView.as_view(), name='detail'),
]