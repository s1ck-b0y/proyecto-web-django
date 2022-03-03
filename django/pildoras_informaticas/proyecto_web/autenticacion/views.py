from django.shortcuts import render
from django.views.generic import View
# Create your views here.

from django.contrib.auth.forms import UserCreationForm

class VRegistro(View):
    def get(self,request):
        form=UserCreationForm()
        return render(request,"registro/registro.html",{"form":form})

    def post(self,request):
        pass