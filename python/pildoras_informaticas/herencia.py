class Vehiculos():
    def __init__(self, marca, modelo):
        self.marca=marca
        self.modelo=modelo
        self.en_marcha=False
        self.acelera=False
        self.frena=False

    def arrancar(self):
        self.en_marcha=True
        
    def acelerar(self):
        self.acelera=True

    def frenar(self):
        self.frena=True

    def estado(self):
        print("Marca: ", self.marca, "\nModelo: ", self.modelo,
        "\nEn Marcha: ", self.en_marcha, "\nAcelerando: ", self.acelera,
        "\nFrenando", self.frena)

class Furgoneta(Vehiculos):
    def carga(self, cargar):
        self.cargado=cargar
        if(self.cargado):
            return ("La furgoneta está cargada.")
        else:
            return ("La furgoneta no está cargada.")

class Moto(Vehiculos):
    h_caballito="" 
    def caballito(self):
        self.h_caballito="Voy haciendo el caballito"
    def estado(self):
        print("Marca: ", self.marca, "\nModelo: ", self.modelo,
        "\nEn Marcha: ", self.en_marcha, "\nAcelerando: ", self.acelera,
        "\nFrenando", self.frena, "\n", self.h_caballito)

class VElectricos(Vehiculos):
    def __init__(self,marca,modelo):
        super().__init__(marca,modelo)
        self.autonomia=100
    
    def cargarEnergia(self):
        self.cargando=True

mi_moto=Moto("Honda", "CBR")
mi_moto.caballito()
mi_moto.estado()

mi_furgoneta=Furgoneta("Renault", "Kangoo")
mi_furgoneta.arrancar()
mi_furgoneta.estado()
print(mi_furgoneta.carga(True))

class BicicletaElectrica(VElectricos,Vehiculos):
    pass

mi_bici=BicicletaElectrica("Orbea", "IHJ")
