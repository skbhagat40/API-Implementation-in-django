from django.conf.urls import url,include
from . import views
from django.urls import path

urlpatterns = [url(r'^$',views.StockList.as_view(),name='index'),
               path('api-auth/', include('rest_framework.urls')),]
