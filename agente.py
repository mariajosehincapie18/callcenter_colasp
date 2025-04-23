from prioridadmensajes import Prioridad_mensajes
from pmensajes import Procesadormensaje

class Agente ():

    niveles_de_experiencia= {"experimentado": 0.5, "intermedio": 0.75, "basico": 1.0}

    def __init__(self, id:int, nivel_de_experiencia):
        self.id = id
        self.nivel_de_experiencia = nivel_de_experiencia.lower()
        self.estado = "disponible"
        self.valor_experiencia =  Agente.niveles_de_experiencia.get(self.nivel_de_experiencia, 1.0 )
        self.prioridad = Prioridad_mensajes()
        
        

    def calcular_tiempo_estimado(self,mensaje: str):
    
        longitud_mensaje = len(mensaje)
        peso_palabras= self.prioridad.calcular_prioridad(mensaje)


        tiempo_estimado = (longitud_mensaje/ 10) + (peso_palabras / 2)
        tiempo_por_experiencia = tiempo_estimado * self.valor_experiencia

        return tiempo_por_experiencia

   


    










    