# Es un conjunto de datos donde se pierde el factor posicion
# Los vamos a referenciar por clave
# Teniendo un conjunto clave: valor
alumno = {
    "nombre": "Paula de Juan",
    "edad":  38,
    "telefono": 722303820,
}
# print(alumno) imprime el diccionario completo (como el objeto)
# obtenemos el valor poniendo su clave asociada
print(alumno["nombre"])

# getters
print(alumno.get("edad")) # 38

alumno["telefono"] = 722303820

alumno["direccion"] = "Calle Fray Luis de Leon"

# eliminar
alumno.pop("direccion") # eliminamos esa clave con su valor


# diccionario complejo
producto = {
    "titulo" : "Portail HP",
    "precio" : 1200,
    "caracteristicas" : {
        "ram" : 16,
        "procesador" : "AMD RYZEN 7",
        "disco": [ 256, 512 ],
    },
    "pantalla" : ["1920", "1980"],
}

# producto(["caracteristicas"]["ram"]) = 32
print(producto(["caracteristicas"]["ram"]))
print(producto(["pantalla"][0]))
print(producto(["pantalla"][0]))
print(producto(["caracteristicas"]["disco"][0]))

# for i in range(len(producto(["caracteristicas"]["disco"]))):
    # print(producto(["caracteristicas"]["disco"][i]))

