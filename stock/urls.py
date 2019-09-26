#from django.conf.urls import url, include
from django.urls import path, include
from django.contrib import admin
from rest_framework.routers import DefaultRouter
from stock import views
from stock.views import StockListView, StockDetail, StockCreateView, StockUpdateView, StockDeleteView

app_name = 'stocks'

router = DefaultRouter()
router.register(r'info', views.StockViewSet)

urlpatterns = [
    #For Django 1.x
    #url(r'^admin/', admin.site.urls),
    #url(r'^api/', include(router.urls))
    path('', include(router.urls)),
    path('view', StockListView.as_view(), name="index"),
    path('<int:pk>/', StockDetail.as_view(), name="stock_id"),
    path('create/', StockCreateView.as_view(), name="create"),
    path('<int:pk>/update/', StockUpdateView.as_view(), name="update"),
    path('<int:pk>/delete/', StockDeleteView.as_view(), name="delete"),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]