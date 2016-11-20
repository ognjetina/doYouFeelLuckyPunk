from django.conf.urls import url
from rasp_do_you_feel_lucky_punk_web import views

# patterns here are prefixed with 'web/'
urlpatterns = [
    url(r'^.*$', views.is_ps3_online),
    ]
