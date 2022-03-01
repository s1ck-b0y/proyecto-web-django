import email
from django.shortcuts import render,redirect

from django.core.mail import EmailMessage

from .forms import FormularioContacto

# Create your views here.

def contacto(request):
    formulario_contacto=FormularioContacto()

    if (request.method == "POST"):
        formulario_contacto=FormularioContacto(data=request.POST)
        if (formulario_contacto.is_valid):
            nombre=request.POST.get("nombre")
            email=request.POST.get("email")
            contenido=request.POST.get("contenido")

            email=EmailMessage("Mensaje desde app Django",
            "El usuario con nombre {} con la dirección {} escribe lo siguiente:\n\n {}".format(nombre,email,contenido),"",["maxi.barreneche@gmail.com"],reply_to=[email])

            try:
                email.send() 

                return redirect("/contacto/?valido")
            except:
                return redirect("/contacto/?no_valido")

    return render(request,"contacto/contacto.html",{"formulario":formulario_contacto})