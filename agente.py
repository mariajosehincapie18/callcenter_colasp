from prioridadmensajes import Prioridad_mensajes
from pmensajes import Procesadormensaje

class Agente ():

    niveles_de_experiencia= {"experto": 0.5, "intermedio": 0.75, "basico": 1.0}

    def __init__(self, id:int, nivel_de_experiencia):
        self.id = id
        self.nivel_de_experiencia = nivel_de_experiencia.lower()
        self.estado = "disponible"
        self.valor_experiencia =  Agente.niveles_de_experiencia.get(self.nivel_de_experiencia, 1.0 )
        
        

    def calcular_tiempo_estimado(self,mensaje: str):
        prioridad= Prioridad_mensajes()
        longitud_mensaje = len(mensaje.split())
        peso_palabras= prioridad.calcular_prioridad(mensaje)


        tiempo_estimado = (longitud_mensaje/ 10) + (peso_palabras / 2)
        tiempo_por_experiencia = tiempo_estimado * self.valor_experiencia

        return tiempo_por_experiencia
    

consultas_experto = Agente(151, "experto")
consultas_intermedio = Agente(151, "intermedio")
consultas_basico = Agente(151, "basico")

mensaje_prueba= ("hola buenas tardes necesito ayuda")

print(consultas_experto.calcular_tiempo_estimado(mensaje_prueba ))
print(consultas_intermedio.calcular_tiempo_estimado(mensaje_prueba ))
print(consultas_basico.calcular_tiempo_estimado(mensaje_prueba ))









    