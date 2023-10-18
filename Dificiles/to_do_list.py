#Sistema de lista de tareas
def agregar_tareas(inventario):
    try: 
        titulo = input("Ingrese el titulo de la tarea: ")
        descripcion = input("Ingrese la descripción de la tarea: ")

        tarea = {"titulo": titulo, "descripcion": descripcion}
        inventario.append(tarea)
        print("Se agregó la tarea con exito")
    except:
        print("Error al agregar la tarea")

def listar_tareas(inventario):
    #Valido si hay tareas en el inventario
    if not inventario:
        print("No hay tareas registradas\n")
    else:
        print("\nLista de tareas")
        
        for indice, tarea in enumerate(inventario):
            print(indice,". -",tarea["titulo"], "descripcion", tarea["descripcion"])

def actualizar_tareas(inventario):
    listar_tareas(inventario)
    if not inventario:
        return
    else:
        try:
            indice = int(input("Ingrese el indice de la tarea a actualizar: "))
            if(indice < 0 or indice > len(inventario)):
                print("El indice no existe en la lista.")
            else: 

                titulo = input("Ingrese el nuevo nombre de la tarea: ")
                descripcion = input("Ingrese la nueva descripcion de la tarea: ")
                print("Actualizando el producto",inventario[indice]["titulo"])

                inventario[indice]["titulo"] = titulo
                inventario[indice]["descripcion"] = descripcion

                print("\nEl producto fue actualizado con exito!\n")

        except:
            print("Oops!, algo salió mal")

def eliminar_tarea(inventario):
    listar_tareas(inventario)

    if not inventario:
        return
    else:
        try:
            indice = int(input("Ingrese el indice de la tarea a eliminar: "))
            if(indice < 0 or indice > len(inventario)):
                print("El indice no corresponde a ninguna tarea\n")
            else:
                print("Eliminando tarea ...")
                inventario.pop(indice)
                print("La tarea fue eliminado con éxito.\n")
        except:
            print("Oops!, algo salió mal")

def mostrarMenu():
    input("Presione ENTER para continuar...")
    print("\n----------MENÚ DE OPCIONES----------\n")
    print("1. Listar tareas")
    print("2. Agregar productos")
    print("3. Actualizar producto")
    print("4. Eliminar producto")
    print("5. Salir")

def main():
    inventario = []
    while True:
        
        mostrarMenu()
        opcion = input("Ingrese una opción: ")

        if(opcion == "1"):
            listar_tareas(inventario)

        elif(opcion == "2"):
            agregar_tareas(inventario)
        
        elif(opcion == "3"):
            actualizar_tareas(inventario)

        elif(opcion == "4"):
            eliminar_tarea(inventario)
            
        elif(opcion == "5"):
            break
        

main()