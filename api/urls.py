from django.conf.urls import include, url
from . import views

urlpatterns = [
              url(r'^loan$',views.loan),
               url(r"", views.loan),

               ]
