import time
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
        b = print(f"\nEn la sección de {i}, se tienen los siguientes productos:\n")
        for j in lista[i]:
           a = print(f"-->{j}:\n  -Precio: ${lista[i][j]["precio"]}\n -Cantidad disponible en tienda: {lista[i][j]["Cantidad en tienda"]} unidades.\n ")

def Modificar_inventarios(lista, Sección:str, Opcion:int, Nombre_producto:str, Nuevo_valor:int ):
    if Opcion == 1:
        lista['Sección']['Nombre_producto']["precio"] = Nuevo_valor
    elif Opcion == 2:
        lista['Sección']['Nombre_producto']['Cantidad'] = Nuevo_valor
    print('\n Este es el inventario actualizado:')
    for i in lista:
        b = print(f"\nEn la sección de {i}, se tienen los siguientes productos:\n")
        for j in lista[i]:
           a = print(f"-->{j}:\n  -Precio: ${lista[i][j]["precio"]}\n -Cantidad disponible en tienda: {lista[i][j]["Cantidad en tienda"]} unidades.\n ")
    
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
            "precio" : 10000000000,
            "Cantidad en tienda": 3
        }
    }
}
