# Quiero unir hacer un import de trabajadores.py
# Usamos el sistema from
from data.trabajadores import trabajadores

# Queremos calcular por cada trabajador lo que cuestan sus horas extra 
# Función que reciba 1 trabajador y calcule su hora extra y lo añada como:
# "coste_hora_extra" : $

def calcular_coste_hora_extra(trabajador):
    # dividimos el sueldo entre las horas_contrato y sacamos el coste_hora
    # Multiplicamos por las horas extra y obtenermos el coste de las horas extra
    # Se lo añadimos al trabajador clave:valor
    
    precio_hora = trabajador["sueldo_base"] / trabajador["horas_contrato"]
    total_horas_extra = trabajador["horas_extra"] * precio_hora 
    trabajador["coste_horas_extra"] = total_horas_extra
    print(total_horas_extra)

for trabajador in trabajadores:
    calcular_coste_hora_extra(trabajador)

# sueldo base - menos porcentaje % de impuestos + suma total horas extra