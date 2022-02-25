def devuelveCiudades(*ciudades):
    for elemento in ciudades:
        # for sub_elemento in elemento: 
            # yield sub_elemento
        yield from elemento

ciudades_devueltas=devuelveCiudades("Madrid", "Barcelona", "Bilbabo", "Valencia")
print(next(ciudades_devueltas))
print(next(ciudades_devueltas))
