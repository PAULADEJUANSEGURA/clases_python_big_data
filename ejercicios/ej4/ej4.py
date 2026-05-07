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
    trabajador["total_horas_extra"] = total_horas_extra
    print(total_horas_extra)


# sueldo base - menos porcentaje % de impuestos + suma total horas extra
def calcular_nomina(trabajador):
    irpf = trabajador['sueldo_base'] * (trabajador['porcentaje_impuestos']/100)
    sueldo_neto_sin_extras = trabajador['sueldo_base'] - irpf
    sueldo_final = sueldo_neto_sin_extras + trabajador['total_horas_extra']
    trabajador['nomina'] = sueldo_final




for trabajador in trabajadores:
    calcular_coste_hora_extra(trabajador)
    calcular_nomina(trabajador)


# print(trabajadores)

# pintar todos los trabajadores de la lista
def imprimir_trabajadores(trabajadores):
    for trabajador in trabajadores:
       print(f"ID Trabajador: {trabajador["id"]}")
       print(f"Nombre Trabajador: {trabajador["nombre"]}")
       print(f"Departamento Trabajador: {trabajador["departamento"]}")
       print(f"Sueldo base: {trabajador["sueldo_base"]}") 
       print(f"Horas de contrato: {trabajador["horas_contrato"]}")
       print(f"Horas extra: {trabajador["horas_extra"]}")
       print(f"Porcentaje impuestos IRPF: {trabajador["porcentaje_impuestos"]}")
       print(f"Coste hora extra: {trabajador['total_horas_extra']}") 
       print(f"Cálculo de la nómina del trabajador: {trabajador['nomina']}")
       print("-"*60)



# filtrar los trabajadores y pintarlos por categoria = departamento
def imprimir_trabajadores_por_departamento(trabajadores):
    for trabajador in trabajadores:
        print(f"Nombre Trabajador: {trabajador["nombre"]}")
        print(f"Categoria Departamento: {trabajador["departamento"]}")
        print("-"*60)

print("---# Imprimir trabajadores #----")
imprimir_trabajadores(trabajadores)
print("---# Imprimir Departamentos #----")
imprimir_trabajadores_por_departamento(trabajadores)