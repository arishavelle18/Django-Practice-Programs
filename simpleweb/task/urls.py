from django.urls import path

from . import views

# avoid name collision of template
app_name ='task'

urlpatterns = [
    path("",views.index,name="index"),
    path("add",views.add,name="add")

]