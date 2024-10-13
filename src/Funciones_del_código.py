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

inventarios = {
    "Mecatos": {
        'papas de limon': {
            "precio": 2500, 
            "cantidad en tienda": 5 
        },        
        'Galletas': {
            "precio": 1800,
            "Cantidad en tienda": 20
        },
        "Chocolatina":{
            "precio": 850,
            "Cantidad en tienda": 50
        },
    "Aseo y hogar":{
        "Fabuloso":{
            "Precio": 10000,
            "Cantidad en tienda": 20
        },
        "Shampoo": {
            "Precio": 15000,
            "Cantidad en tienda": 16
        },
    },
    "Productos varios":{
        "f22 raptor":{
            "Precio" : 10000000000,
            "Cantidad en tienda": 3
        }
    }
    },
}

