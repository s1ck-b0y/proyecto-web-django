class Carro:
    def __init__(self,request):
        self.request=request
        self.session=request.session
        carro=self.session.get("carro")

        if (not carro):
            carro=self.session["carro"]={}
        else:
            self.carro=carro;

    def agregar(self,producto):
        if (str(producto.id) not in self.carro.keys()):
            self.carro[producto.id]= {
                "producto_id":producto.id,
                "nombre":producto.nombre,
                "precio": str(producto.precio),
                "cantidad":1,
                "imagen":producto.imagen.url
            }
        else:
            for (key,value) in self.carro.items():
                if (key == str(producto.id)):
                    value["cantidad"]=value["cantidad"]+1
                    break
        
        self.guardarCarro()

    def guardar_carro(self):
        self.session["carro"]=self.carro
        self.session.modified=True

    def eliminar(self,producto):
        producto.id=str(producto.id)
        if (producto.id) in self.carro:
            del self.carro[producto.id]
            self.guardar_carro()

    def restarProducto(self,producto):
        for (key,value) in self.carro.items():
            if (key == str(producto.id)):
                value["cantidad"]=value["cantidad"]-1
                if (value["cantidad"] == 0):
                    self.eliminar(producto)
                break
        self.guardar_carro()
    
    def limpiarCarro(self):
        carro=self.session["carro"]={}
        self.session.modified=True
        