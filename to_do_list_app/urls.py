from django.conf.urls import url

from to_do_list_app import views

urlpatterns = [
    url(r'^$', views.index, name="index"),
]
