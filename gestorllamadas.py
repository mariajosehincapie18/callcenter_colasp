import threading
import time
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
        self.hilos_activos = []
        

    def recibir_mensaje(self):
        resultados = self.procesador.procesar_mensaje()
        if resultados:
            for _, prioridad, mensaje in resultados:
                self.cola_mensaje.enqueue( (prioridad, mensaje))
        

        cola = self.cola_mensaje._PriorityQueue__queue
        for i, mensaje in enumerate(cola, start=1):
            print(f"{i}. {mensaje}")

    def mensaje_mas_largo_y_mas_corto(self):
        cola = self.cola_mensaje._PriorityQueue__queue

        if len(cola) == 0:
            print("no hay mensaje")
 
        grupos = {}
        for prioridad, mensaje  in cola:
            if prioridad in grupos:
                grupos[prioridad].append(mensaje)
            else:
                grupos[prioridad]= [mensaje]

    
        orden_prioridad = sorted(grupos, key=lambda x: len(grupos[x]))
        grupo_mas_pequeño = orden_prioridad[0]
        mensaje = grupos[grupo_mas_pequeño]
        if len(grupos[grupo_mas_pequeño]) > 1:
            mensaje_mas_corto = min(mensaje, key= len)
            mensaje_mas_largo = max(mensaje, key= len)
        if len(grupos[grupo_mas_pequeño]) == 1:

            segundo_grupo_pequeño = orden_prioridad[1]
            mensaje1 = grupos[grupo_mas_pequeño][0]
            mensaje2 = grupos[segundo_grupo_pequeño]

            mensaje_mas_corto = min([mensaje1] + mensaje2, key=len)
            mensaje_mas_largo = max([mensaje1] + mensaje2, key= len)

    
    
        print("los grupos son:  ")   
        for prioridad, mensaje in grupos.items():
            print(f"prioridad  {prioridad}: ")
            for mensaje in mensaje:
                print(f"  -  {mensaje}")
        print("ordenes de grupos", orden_prioridad)
        print("grupo mas pequeño: ", grupo_mas_pequeño)
        print("2do grupo mas pequeño: ", segundo_grupo_pequeño)
        print("el mensaje mas corto es", mensaje_mas_corto)
        print("el mensaje mas largo ", mensaje_mas_largo)
        



    
    def obtener_agente_disponible(self, prioridad_actual):

            
            for agente in self.agentes:
                if agente.estado == "disponible" and agente.nivel_de_experiencia == "experimentado":
                    return agente
            
            for agente in self.agentes:    
                if agente.estado == "disponible" and agente.nivel_de_experiencia == "intermedio":
                    return agente     
            for agente in self.agentes:    
                if agente.estado == "disponible" and agente.nivel_de_experiencia == "basico":
                    return agente    
                    
                
            return None
                        
    def atender_mensaje(self, agente, mensaje, prioridad):
        tiempo = agente.calcular_tiempo_estimado(mensaje)
        print(f"AGENTE {agente.id} ({agente.nivel_de_experiencia}) atiende el mensaje: {mensaje} (prioridad {prioridad}) en {tiempo:.2f}seg.")
        
        time.sleep(tiempo)
        agente.estado = "disponible"
        print(f"AGENTE {agente.id} esta de nuevo disponible")


    def asignar_llamadas(self):
        while len(self.cola_mensaje) > 0:
            try:
                prioridad, mensaje = self.cola_mensaje.dequeue()
                agente= self.obtener_agente_disponible(prioridad)
                if agente:
                    agente.estado= "ocupado"
                    hilo = threading.Thread(target=self.atender_mensaje, args=(agente,mensaje, prioridad))
                    hilo.start()
                    self.hilos_activos.append(hilo)
   
                else:
                    print("No hay agentes disponibles. Mensaje reencolado")
                    self.cola_mensaje.enqueue((prioridad, mensaje))
                    time.sleep(1)
                
            except EmptyQueue:
                break

    def finalizacion(self):
        for hilo in self.hilos_activos:
            hilo.join()

    
     

  
     
    
    