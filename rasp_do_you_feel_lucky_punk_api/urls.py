from django.conf.urls import url
from rasp_do_you_feel_lucky_punk_api import views

urlpatterns = [
    url(r'^hello_world$', views.hello_world)
    ]
