import time
from os import system
def Bloqueo_de_seguridad(segundos:float):
        while segundos:
            mins = segundos // 60
            sge = segundos 
            tiempo_restante = f"{mins:02d}:{sge:02d}"
            print(f"{tiempo_restante} segundos", end="\r")
            time.sleep(1)
            segundos -= 1
        return(tiempo_restante)

def Imprimir_inventarios(lista):
    for i in lista:
        print(f"\nEn la sección de {i}, se tienen los siguientes productos:\n")
        for j in lista[i]:
            print(f"-->{j}:\n  -Precio: ${lista[i][j]["precio"]}\n -Cantidad disponible en tienda: {lista[i][j]["Cantidad en tienda"]} unidades.\n ")

def Modificar_inventarios(lista, Sección:str, Opcion:int, Nombre_producto:str, Nuevo_valor:float ):
    if Opcion == 1:
        lista[Sección][Nombre_producto]['precio'] = Nuevo_valor
        system('cls')
        print('\n Esta es la sección del inventario actualizada:\n')
        print(f'{Sección}:\n')
        print(f'{Nombre_producto}:')
        print(f' -Precio: {lista[Sección][Nombre_producto]['precio']}\n -Cantidad disponible en tienda: {lista[Sección][Nombre_producto]["Cantidad en tienda"]}')
    elif Opcion == 2:
        lista[Sección][Nombre_producto]['Cantidad en tienda'] = Nuevo_valor
        system('cls')
        print('\n Esta es la sección del inventario actualizada:')
        print(f'{Sección}:\n')
        print(f'{Nombre_producto}:')
        print(f' -Precio: {lista[Sección][Nombre_producto]['precio']}\n -Cantidad disponible en tienda: {lista[Sección][Nombre_producto]["Cantidad en tienda"]}')


inventarios = {
    "Mecatos":{
        "Papas de limon": {
            "precio": 23, 
            "Cantidad en tienda": 5 
        },        
        'Galletas':  {
            "precio": 1800,
            "Cantidad en tienda": 20
        },
        "Chocolatina":{
            "precio": 850,
            "Cantidad en tienda": 50
        },
    },
    "Aseo":{
        "Fabuloso":{
            "precio": 10000,
            "Cantidad en tienda": 20
        },
        "Shampoo": {
            "precio": 15000,
            "Cantidad en tienda": 16
        },
    },
    "Variedades":{
        "f22 raptor":{
            "precio" : 1,
            "Cantidad en tienda": 3
        }
    }
}