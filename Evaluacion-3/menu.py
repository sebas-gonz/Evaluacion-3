import biblioteca
import os,json
def menu():
    while True:
        os.system('cls')
        print("*" * 33)
        print("*        Mundo libro          ")
        print("*" * 33)
        print()
        print()
        print("[1] - Mantenedor de autores")
        print("[2] - Reportes")
        print("[3] - Salir")
        try:
            opc = int(input("Seleccione una opcion: "))
            if opc == 1:
                biblioteca.mantenedor_autores()
            elif opc == 2:
                biblioteca.cantidad_libros_prestados()
            elif opc == 3:
                return
            else:
                print("La opcion no existe.")
                input("Presione enter para continuar.")
        except ValueError:
            print("Dato incorecto.")
            input("Presione enter para continuar.")
menu()