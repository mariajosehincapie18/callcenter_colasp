from prioridadmensajes import Prioridad_mensajes 
from priority_cola import PriorityQueue, EmptyQueue
from agente import Agente
from pmensajes import Procesadormensaje
import os

class Gestorllamadas():
    def __init__(self, agentes, ruta_mensaje):
        self.agentes = sorted(agentes, key= lambda a: a.valor_experiencia, reverse=True)
        self.cola_mensaje = PriorityQueue(priority="max")
        self.ruta_mensaje = ruta_mensaje
        self.procesador = Procesadormensaje(ruta_mensaje)
        self.prioridades = []
        

    def recibir_mensaje(self):
        resultados = self.procesador.procesar_mensaje()
        for _, prioridad, mensaje in resultados:
            self.cola_mensaje.enqueue( (prioridad, mensaje))
            self.prioridades.append(prioridad)
    
        print(self.cola_mensaje)

    def asignar_llamadas(self):
        while len(self.cola_mensaje) > 0:
            try:
                prioridad, mensaje = self.cola_mensaje.dequeue()
                agente= self.obtener_agente_disponible()
                if agente:
                    tiempo = agente.calcular_tiempo_estimado(mensaje)
                    print(f"AGENTE {agente.id} ({agente.nivel_de_experiencia}) atiende el mensaje: {mensaje} (prioridad {prioridad}) en {tiempo:.2f}seg.")
                    agente.estado = "ocupado"
                else:
                    print("No hay agentes disponibles")
                    break
            except EmptyQueue:
                break
    
    def obtener_agente_disponible(self):
        for prioridad in self.prioridades:
            if prioridad > 25:


                for agente in self.agentes:
                    if agente.estado == "disponible" and agente.nivel_de_experiencia == "experimentado":
                        return agente
                    
                    elif agente.estado == "disponible" and agente.nivel_de_experiencia == "intermedio":
                        return agente
                    
        
                 
                    
            else:
                for agente in self.agentes:
                    agente.estado == "disponible"
                    return agente
                
        return None
                        
             



     
    
    