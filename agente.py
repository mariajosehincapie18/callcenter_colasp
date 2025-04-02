from prioridadmensajes import Prioridad_mensajes
from pmensajes import Procesadormensaje

class Agente ():

    niveles_de_experiencia= {"Basico": 1.0, "intermedio": 0.75, "Experto":0.50}

    def __init__(self, id:int, niveles_de_experiencia):
        self.id = id
        self.niveles_de_experiencia = niveles_de_experiencia.lower()
        self.estado = "disponible"
        self.valor_experiencia =  Agente.niveles_de_experiencia.get(self.niveles_de_experiencia,1.0 )
        
        

    def calcular_tiempo_estimado(self,mensaje: str):
        prioridad= Prioridad_mensajes()
        longitud_mensaje = len(mensaje.split())
        peso_palabras= prioridad.calcular_prioridad(mensaje)


        tiempo_estimado = (longitud_mensaje/ 10) + (peso_palabras / 2)
        tiempo_por_experiencia = tiempo_estimado * self.valor_experiencia

        return tiempo_por_experiencia
    

consultas = Agente(111, "experto")
mensaje_prueba= ("nesesito ayuda mi celular no funciona y necesito llamar a urgencias")
print(consultas.calcular_tiempo_estimado(mensaje_prueba ))









    