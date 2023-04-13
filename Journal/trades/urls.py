from django.urls import path,include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.index, name='index'),
    path('data', views.dashboard, name= 'dashboard'),
    # path("",views.add_new_trade, name="update_trade")
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



