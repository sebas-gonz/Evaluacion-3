import os,json



def mantenedor_autores():
    while True:
        os.system('cls')
        print("*" * 33)
        print("*        Mantenedor Autores          ")
        print("*" * 33)
        print()
        print()
        print("[1] - Agregar autor")
        print("[2] - Editar autor")
        print("[3] - Eliminar autor")
        print("[4] - Buscar autor")
        print("[5] - Volver")
        try:
            opc = int(input("Seleccione una opcion: "))
            if opc == 1:
                agregar_autor()
            elif opc == 2:
                editar_autor()
            elif opc == 3:
                eliminar_autor()
            elif opc == 4:
                buscar_autor()
            elif opc == 5:
                return
            else:
                print("La opcion no existe.")
                input("Presione enter para continuar.")
        except ValueError:
            print("Dato incorecto.")
            input("Presione enter para continuar.")

def agregar_autor():
    with open("biblioteca.json", mode="r",encoding='utf8') as biblioteca_json:
        biblioteca = json.load(biblioteca_json)
    nombre = input("Ingrese el nombre del nuevo autor: ")
    nacionalidad = input("Ingrese la nacionalidad del nuevo autor: ")
    autor = {
            'AutorID' : len(biblioteca['Autor']) + 1,
            'Nombre' : nombre,
            'Nacionalidad' : nacionalidad
        }
    biblioteca['Autor'].append(autor)
    with open("biblioteca.json", mode="w",encoding='utf8') as biblioteca_json:
        json.dump(biblioteca,biblioteca_json,indent=4)
    print("Se ha agregado con exito el nuevo autor.")
    input("Presione enter para continuar.")

def encontrar_editor(id):
    with open("biblioteca.json", mode="r",encoding='utf8') as biblioteca_json:
        biblioteca = json.load(biblioteca_json)
    autor = None
    for i in range(len(biblioteca['Autor'])):
        if biblioteca['Autor'][i]['AutorID'] == id:
            autor = biblioteca['Autor'][i]
            break
    return autor

def editar_autor():

    with open("biblioteca.json", mode="r",encoding='utf8') as biblioteca_json:
        biblioteca = json.load(biblioteca_json)
    try:
        id = int(input("Ingrese el ID del autor que desea editar: "))
        autor = encontrar_editor(id)
        if autor is not None:
            print(f"AutorID: {autor['AutorID']}")
            print(f"Nombre: {autor['Nombre']}")
            print(f"Nacionalidad: {autor['Nacionalidad']}")
            print("[1] - Editar")
            print("[2] - Cancelar")
            try:
                opc = int(input("Seleccione una opcion."))
                if opc == 1:
                    for i in range(len(biblioteca['Autor'])):
                        if biblioteca['Autor'][i]['AutorID'] == autor['AutorID']:
                            biblioteca['Autor'][i]['Nombre'] = input("Ingrese un nuevo nombre para el autor: ")
                            biblioteca['Autor'][i]['Nacionalidad'] = input("Ingrese un nueva nacionalidad para el autor")
                    with open('biblioteca.json',mode='w',encoding='utf8') as biblioteca_json:
                        json.dump(biblioteca,biblioteca_json,indent=4)
                    print(f"Se ha editado con exito el autor con ID: {autor['AutorID']}")
                    input("Presione enter para continuar.")
                    return
                elif opc == 2:
                    return
                else:
                    print("La opcion no existe.")
                    input("Presione enter para continuar.")
            except ValueError:
                print("Dato incorecto.")
                input("Presione enter para continuar.")
        else:
            print("El autor no existe.")
            input("Presione enter para continuar.")
    except ValueError:
        print("Dato incorecto.")
        input("Presione enter para continuar.")

def eliminar_autor():
    while True:
        os.system('cls')
        with open("biblioteca.json", mode="r",encoding='utf8') as biblioteca_json:
            biblioteca = json.load(biblioteca_json)
        try:
            id = int(input("Ingrese el ID del autor que desea eliminar: "))
            autor = encontrar_editor(id)
            if autor is not None:
                print(f"AutorID: {autor['AutorID']}")
                print(f"Nombre: {autor['Nombre']}")
                print(f"Nacionalidad: {autor['Nacionalidad']}")
                print("[1] - Eliminar")
                print("[2] - Cancelar")
                try:
                    opc = int(input("Seleccione una opcion."))
                    if opc == 1:
                        for i in range(len(biblioteca['Autor'])):
                            if biblioteca['Autor'][i]['AutorID'] == autor['AutorID']:
                                biblioteca['Autor'].pop(i)
                        with open('biblioteca.json',mode='w',encoding='utf8') as biblioteca_json:
                            json.dump(biblioteca,biblioteca_json,indent=4)
                        print(f"Se ha eliminado con exito el autor con ID: {autor['AutorID']}")
                        input("Presione enter para continuar.")
                        return
                    elif opc == 2:
                        return
                    else:
                        print("La opcion no existe.")
                        input("Presione enter para continuar.")
                except ValueError:
                    print("Dato incorecto.")
                    input("Presione enter para continuar.")
            else:
                print("El autor no existe.")
                input("Presione enter para continuar.")
                return
        except ValueError:
            print("Dato incorecto.")
            input("Presione enter para continuar.")

def buscar_autor():
    os.system('cls')
    with open("biblioteca.json", mode="r",encoding='utf8') as biblioteca_json:
        biblioteca = json.load(biblioteca_json)
    for i in range(len(biblioteca['Autor'])):
        print("AutorID", "Nombre", "Nacionalidad")
        print(f"{biblioteca['Autor'][i]['AutorID']},  {biblioteca['Autor'][i]['Nombre']}, {biblioteca['Autor'][i]['Nacionalidad']}")
        print()
    input("Presione enter para continuar.")

def reporte():
    with open("biblioteca.json", mode="r",encoding='utf8') as biblioteca_json:
        biblioteca = json.load(biblioteca_json)
    print("*" * 55)
    print
def cantidad_libros_prestados():
    with open("biblioteca.json", mode="r",encoding='utf8') as biblioteca_json:
        biblioteca = json.load(biblioteca_json)
    datos = {
            'Autor': []
            }
    for i in range(len(biblioteca['Autor'])):
        libros_prestados = 0
        for j in range(len(biblioteca['Libro'])):
            for k in range(len(biblioteca['Prestamo'])):
                if biblioteca['Libro'][j]['LibroID'] == biblioteca['Prestamo'][k]['LibroID']:
                    if biblioteca['Autor'][i]['AutorID'] == biblioteca['Libro'][j]['AutorID']:
                        libros_prestados = libros_prestados + 1
        print("*" * 55)
        print("*       Autor              Cantidad de libros prestados")
        print("*" * 55)
        print(f"{biblioteca['Autor'][i]['Nombre']}", "                          " ,f"{libros_prestados}" )
        autores_libros = {
                'Nombre' : biblioteca['Autor'][i]['Nombre'],
                'Libros_prestados' : libros_prestados
            }
        datos["Autor"].append(autores_libros)
    with open("librosprestados.json", mode="w",encoding='utf8') as libros_prestados:
        json.dump(datos,libros_prestados,indent=4)
    input("Presione enter para continuar.")