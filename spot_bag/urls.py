from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = "spot_bag"
urlpatterns = [
    path("", views.home_page, name="home_page"),
    # path("upload/", views.upload_trades, name="trades"),
]
