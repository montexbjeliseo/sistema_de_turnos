# Tarea 1
# Crear un función que solicite la entrada de:
# Nombre
# Apellido
# DNI

# Funcion para solicitar los datos
def solicitar_datos():
    nombre = input("Nombre: ")
    apellido = input("Apellido: ")
    dni = input("DNI: ")
    return {
        "nombre": nombre,
        "apellido": apellido,
        "dni": dni
    }
# Prueba Tarea 1 
# print(solicitar_datos())
