from .carro import Carro

def importeTotalCarro(request):
    total=0
    carro=Carro(request)

    # if (request.user.is_authenticated):
    for (key,value) in request.session["carro"].items():
        total=total+float(value["precio"])
        
    return {"importeTotalCarro":total}