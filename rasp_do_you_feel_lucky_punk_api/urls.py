from django.conf.urls import url
from rasp_do_you_feel_lucky_punk_api import views

urlpatterns = [
    url(r'^is_server$', views.is_server),
    url(r'^.*$', views.is_ps3_online),
    ]
