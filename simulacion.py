from pmensajes import Procesadormensaje
from gestorllamadas import Gestorllamadas
from agente import Agente


agentes = [
    Agente(1, "experimentado"),
    Agente(2, "intermedio"),
    Agente(3, "basico")
]

ruta_mesaje= r"C:\Users\USUARIO\Documents\semestre 3.2\estructura de datos\callcenter_colasp\mensajes"
procesador= Procesadormensaje(ruta_mesaje)
mensaje = procesador.procesar_mensaje()

gestor = Gestorllamadas(agentes)
gestor.recibir_mensaje(mensaje)
gestor.asignar_llamadas()