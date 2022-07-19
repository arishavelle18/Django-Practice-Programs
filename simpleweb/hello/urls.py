from django.urls import path
from . import views


urlpatterns = [
    path("",views.index,name="index"),
    path("karl",views.karl,name="karl"),
    path("<str:name>",views.greet,name="greet")
]