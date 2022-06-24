from django.urls import path
from .views import *

app_name = "app"

urlpatterns = [
    path("",home, name="home" ),
    path("premium/", premium, name="premium"),
    path("team/", team, name="team"),
    path("chart/", chart, name="chart"),
    path("contactus/",contact, name="contact"),
    path("succses/", Succses.as_view(), name="succses"),
    path("unfortunate/", Unfortunate.as_view(), name="unfortunate"),
    path("notifactions/", Notifactions.as_view(), name="notifactions"),
    path("sign/", Sign.as_view(), name="sign"),
    path("addchart/", addChart, name="addchart"),
]