import os
import time
os.system("cls")

lista = []
especies = ["perros", "gatos", "caballos", "vacas", "ovejas", "cerdos", "hamster"]

def registrar_mascotas():
    while True:
        try:
            especie = input("Ingrese la especie de su mascota: ")
            while True:
                try:
                    nombre = ("Ingrese el nombre de su mascota: ")
                except:
                    input ("Error de ingreso del nombre.")
            while True:
                try: 
                    peso = int(input("Ingrese el peso de su mascota: "))
                    if peso <0 or peso >10000:
                        input("Error, intente nuevamente")
                    else:
                        impuesto = round (costo*0.05)
                        total = costo + impuesto
                        break
                except:
                    input("Error en ingresar el peso.")
            while True:
                try: 
                    costo = int(input("Ingrese el costo: "))
                    if costo <100 or costo >1000000:
                        input("No es valido, ingrese nuevamente")
                    else:
                        break
                except:
                    input("Error, ingrese nuevamente el costo")
        except:
            input("Error, reingrese.")
            lista.append([especie, nombre, peso, impuesto, total, costo])
            break

titulo = print ("="*30)
print("BIENVENIDO A VETERINARIA DUOC")
print("="*30)
print("")
time.sleep(4)
os.system("cls")


def listar():
    while True:
        try:
            print(f"{titulo}")
            for row in lista:
                print(f"{row[0]:10s}", end="")
                print(f"{row[1]:10s}", end="")
                print(f"{row[2]:10d}", end="")
                print(f"{row[3]:10d}", end="")
                print(f"{row[4]:10d}", end="")
                print("")
        except:
            input("Error de listar")
            break

def imprimir():
   while True:
    try:
        opc = int(input("¿Desea imprimir una o todos los registros? \n1.- Todos los registros. \n2.- Solo un registro.\n3.- Volver al menu principal."))
        if opc == 1:
            with open ("ImprimirOrden.txt", "w", newline='') as archivo:
                archivo.write(titulos+"\n")
                for especie in lista:
                    archivo.write(f"{especie[0]:10s}{especie[1]:10s}{especie[2]:10d}{especie[3]:10d}{especie[4]:10s}\n")
                    input("Lista de mascotas impresa en 'ImprimirOrden.txt'. Presione ENTER para continuar.")
        elif opc == 2:
            ped = input("Ingrese la especie a imprimir: ").lower()
            encontrados = False
            with open ("OrdenEspecie.txt", "w", newline='') as archivo:
                archivo.write(titulo+"\n")
                for especie in lista:
                    if especie[0].lower() == ped:
                        archivo.write(f"{especie[0]:10s}{especie[1]:10s}{especie[2]:10d}{especie[3]:10d}{especie[4]:10s}\n")
                        encontrados = True
                    if not encontrados:
                        input(f"No se encontraron especies de este tipo. '{ped}'. Presione ENTER para continuar.")
                    else:
                        input(f"Lista de mascotas por especies '{ped} impresa en 'OrdenEspecie.txt'. Presione ENTER para continuar. ")
        elif opc == 3:
            break
    except:
        input("ERROR DE IMPRIMIR")


while True:
    os.system("cls")
    try:
        opc = int(input(f'''
{"="*30}
1.- Registrar mascota.
2.-Listar mascota.
3.- Imprimir registro de mascota.
4.-Salir del programa.
{"="*30} \n Digite opcion: '''))
        if opc == 1:
            registrar_mascotas()
        elif opc == 2:
            listar()
        elif opc == 3:
            imprimir()
        elif opc == 4:
            break
    except:
        input("Error, seleccione nuevamente")