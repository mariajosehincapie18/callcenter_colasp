from prioridadmensajes import Prioridad_mensajes 
from priority_cola import PriorityQueue, EmptyQueue
from agente import Agente

class Gestorllamadas():
    def __init__(self, agentes):
        self.agentes = sorted(agentes, key= lambda a: a.valor_experiencia, reverse=True)
        self.cola_mensaje = PriorityQueue(priority="max")
        