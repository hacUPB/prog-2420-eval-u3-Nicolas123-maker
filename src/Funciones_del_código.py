import time
from os import system
def Bloqueo_de_seguridad(segundos:float): #Aprendi a hacer esta funcion en un tutorial de "CPU TIPS" en Youtube, le cambie algunas cosas a la función del tutorial
        while segundos:
            mins = segundos // 60 #Obtiene la parte entera de la division del parametro entre 60 
            sge = segundos 
            tiempo_restante = f"{mins:02d}:{sge:02d}"#Esto asegura que las variables solo tengan dos digitos
            print(f"{tiempo_restante} segundos", end="\r")#End = '\r' sobrescribe o actualiza el valor de las variables en una misma linea
            time.sleep(1)#Detiene el bucle un segundo 
            segundos -= 1
        return(tiempo_restante)

def Imprimir_inventarios(lista):
    for i in lista:#itera en las secciones
        print(f"\nEn la sección de {i}, se tienen los siguientes productos:\n")
        for j in lista[i]:#itera en los productos de cada sección
            print(f"-->{j}:\n  -Precio: ${lista[i][j]["precio"]}\n -Cantidad disponible en tienda: {lista[i][j]["Cantidad en tienda"]} unidades.\n ")

def Modificar_inventarios(lista, Sección:str, Opcion:int, Nombre_producto:str, Nuevo_valor:float ):
    if Opcion == 1:
        lista[Sección][Nombre_producto]['precio'] = Nuevo_valor #Cambia el valor en los parametros ingresados
        system('cls')
        print('\n Esta es la sección del inventario actualizada:\n')#Muestra como quedo la seccion despues del cambio
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
            "precio": 2500, 
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
            "precio" : 10000000000000000,
            "Cantidad en tienda": 3
        }
    }
}