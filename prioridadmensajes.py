

class Prioridad_mensajes():
     
    palabras_claves= {
        "urgente": 10,
        "emergencia":10,
        "auxilio":10, 
        "urgencias":9,
        "inmediato":9,
        "ayuda":8,
        "problema":7,
        "reclamo":6, 
        "consulta":5,
        "demora":4,
        "atencion":3}
    
    def calcular_prioridad(self, mensaje):   
        prioridad= 0      
        for palabra,valor in self.palabras_claves.items():
            if palabra in mensaje:
                prioridad += valor
        print(prioridad)
        return prioridad
    
   

            