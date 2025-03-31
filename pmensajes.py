import os
from prioridadmensajes import Prioridad_mensajes 

class Procesadormensaje():

    def __init__(self, ruta_mensajes):
        self.ruta_mensaje= ruta_mensajes
        self.prioridad = Prioridad_mensajes()


    def procesar_mensaje(self):
        if not os.path.exists(self.ruta_mensaje):
            print(f"la carpeta no existe {self.ruta_mensaje}")
            return
        
        archivos = [i for i in os.listdir(self.ruta_mensaje) if i.endswith(".txt")]

        if not archivos:
            print("no hay arcivos")
            return
        
        resultados = []

        for archivo in archivos:
            ruta_mensaje = os.path.join(self.ruta_mensaje, archivo)
            with open(ruta_mensaje, "r", encoding="utf+8") as i:
                mensaje = i.read().strip()
                prioridad = self.prioridad.calcular_prioridad(mensaje)
                resultados.append((archivo, prioridad))
        
        resultados.sort(key=lambda x: x[1], reverse= True)


        print("\n Mensaje ordenados:")
        for archivo, prioridad in resultados:
            print(f"Archivo:{archivo},  prioridad:{prioridad}")


ruta_mesaje= r"C:\Users\USUARIO\Documents\semestre 3.2\estructura de datos\callcenter_colasp\mensajes"
procesador= Procesadormensaje(ruta_mesaje)
procesador.procesar_mensaje()
