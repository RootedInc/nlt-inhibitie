from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^niet-genoeg/', views.notnuff, name="notnuff"),
    url(r'^doe-de-test/', views.kleurtest, name="test"),
    url(r'^resultaten/', views.resultaten, name="resultaten"),
]