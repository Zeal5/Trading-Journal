from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", views.home_page, name="spot_bag_page"),
    # path("upload/", views.upload_trades, name="trades"),
]
