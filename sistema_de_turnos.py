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

# Tarea 2
# Crear un menú con las siguientes opciones:
# "Ingresar turno"
# "Salir del Sistema"

def menu():
    """
    Imprime el menú del sistema de turnos
    """
    print("*"*40)
    print("Sistema de turnos")
    print("*"*40)
    print("1. Ingresar turno")
    print("2. Salir del sistema")

# Pruba Tarea 2    
# menu()