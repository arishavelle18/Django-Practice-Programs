from django.shortcuts import render
from django import forms
from django.http import HttpResponseRedirect
from django.urls import reverse

tasks= []

class addForm(forms.Form):
    item = forms.CharField(label="Add Task ")
    # priority = forms.IntegerField(label="Priority ", min_value=1,max_value=10)

# Create your views here.



def index(request):
    if "tasks" not in request.session:
        request.session["tasks"] = []
    return render(request,"task/index.html",{
        "tasks": request.session["tasks"]
    })

def add(request):
    if request.method == "POST":
        form = addForm(request.POST)
        if form.is_valid():
            task = form.cleaned_data["item"]
            # if you want to use priority
            # priority = form.cleaned_data["priority"]
            # tasks.insert(priority-1,task)
            # tasks.append(task)
            request.session["tasks"] += [task]
            return HttpResponseRedirect(reverse("task:index"))
        else:
            return render(request,"task/add.html",{
                "addForms" : form
            })
    
    return render(request,"task/add.html",{
        "addForms":addForm
    })
