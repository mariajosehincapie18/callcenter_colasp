from pmensajes import Procesadormensaje
from gestorllamadas import Gestorllamadas
from agente import Agente


agentes = [
    Agente(1, "experimentado"),
    Agente(2, "intermedio"),
    Agente(3, "basico"),
    Agente(4, "experimentado"),
    Agente(5, "intermedio"),
    Agente(6, "basico"),
    Agente(7, "experimentado"),
    Agente(8, "intermedio"),
    Agente(9, "basico")
]

ruta_mesaje= r"C:\Users\USUARIO\Documents\semestre 3.2\estructura de datos\callcenter_colasp\mensajes"
gestor = Gestorllamadas(agentes, ruta_mesaje )
gestor.recibir_mensaje()
gestor.mensaje_mas_largo_y_mas_corto()
gestor.asignar_llamadas()