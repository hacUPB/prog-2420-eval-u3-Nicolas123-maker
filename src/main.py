
def main():
    from os import system
    import time
    import Funciones_del_código
    from Funciones_del_código import inventarios
    contraseña = "Contraseña_predeterminada123"
    control = True
    system('cls')
    while control == True: #Primer bucle de control general 
        lista1 = [1, 2]
        print("1. Cliente\n2.Administrador")
        a = int(input(f"Por favor seleccione su rol (1 o 2): "))
        system("cls")
        if a not in lista1:
            print("Por favor seleccione una opción correcta")
        elif a == 1:
            v_control = True
            print("Hola!, para una experiencia mas personalizada, por favor responda las siguientes preguntas:\n")
            while v_control == True: 
                titulo = str(input(" -->Como prefiere que nos refiramos hacia usted? (sr. o sra):"))
                titulo = titulo.capitalize()
                if titulo not in ["Sr", "Sra"]:
                    system('cls')
                    print("Por favor verifique su respuesta")
                else: 
                    v_control = False
                    system("cls")
                    nombre = str(input(" -->Ingrese su nombre:"))
                    nombre = nombre.capitalize()
                    system('cls')
                    print(f'Bienvenido a la primera tienda virtual de Medellín {titulo}. {nombre}\n')
                    l = str(input("Desea ver los productos que tenemos disponibles para usted? (Si/No):"))
                    l = l.capitalize()
                    if l == "No":
                        break #Detiene la continuidad del código en caso de que el usuario No quiera ver los productos disponibles y por tanto no quiera comprar
                    elif l == "Si":
                        system('cls')
                        print(f"Excelente!, procesando...\n" )
                        print({Funciones_del_código.Bloqueo_de_seguridad(6)}) #Simula una pantalla de carga para la impresion de los inventarios
                        system('cls')
                        Funciones_del_código.Imprimir_inventarios(inventarios)
                    elif l not in ["Si", "No"]:
                        print("La respuesta ingresada no se encuentra dentro de las opciones disponibles")
                    v_de_respuesta= True
                    Precio_total = 0 #Acumula los precios de los productos seleccionados
                    while v_de_respuesta == True:
                        Sección_producto = str(input("\nEn que sección se encuentra el producto que deseas comprar? (Mecatos, Aseo, Variedades): "))
                        print(Funciones_del_código.Imprimir_inventarios)
                        system('cls')
                        Sección_producto = Sección_producto.capitalize()
                        print(f'Excelente! Estos son los productos disponibles en la sección {Sección_producto}: \n')
                        for producto in inventarios[Sección_producto]:
                            print(f'{producto}\n -->Precio: {inventarios[Sección_producto][producto]['precio']}$\n -->Cantidad disponible en tienda: {inventarios[Sección_producto][producto]['Cantidad en tienda']}')
                        Producto_compra = str(input("\nQue producto deseas comprar? (Asegúrate de copiarlo tal cual aparece en la pantalla): ")) 
                        if Producto_compra not in inventarios[Sección_producto]:
                            print("Escribiste mal el producto o este no está disponible por el momento")
                        else:
                            Continuación_de_compra = str(input('Deseas seguir comprando? (Si/No):'))
                            Continuación_de_compra = Continuación_de_compra.capitalize()
                            Precio_total += inventarios[Sección_producto][Producto_compra]['precio']
                            if Continuación_de_compra == 'No':
                                system('cls')
                                print(f"El valor total de la compra es de {Precio_total}$\nGracias por comprar en la primera tienda virtual de Medellín {titulo}. {nombre}.")
                                v_de_respuesta = False
                            elif Continuación_de_compra == 'Si':
                                system('cls') #Despeja la terminal para que no se sature con la continuidad del while
            control = False 
        elif a == 2:
            system("cls")
            control = False
            cont = str(input("Por favor ingrese su contraseña: "))
            system("cls")
            if cont != contraseña:
                print("Contraseña incorrecta, intetalo nuevamente dentro de\n")
                Tiempo_bloqueo = Funciones_del_código.Bloqueo_de_seguridad(20)  #Tiempo de bloqueo en caso de ingresar mal la contraseña  
                break          
            else: 
                Control2 = True
                while Control2 == True:
                    print("Hola Administrador/a, ¿qué deseas hacer?\n 1.Cambiar la contraseña\n 2.Editar los inventarios")
                    z = int(input("Selecciona una opción (1 o 2): "))
                    system("cls")
                    if z not in (1,2):
                        print("Por favor seleccione una opción correcta")
                        Control2 = True
                    elif z == 1:
                        print(f"Recuerda que la contraseña acutual es: {contraseña!r}")
                        contraseña = str(input("Ingresa la nueva contraseña:")) 
                        print("¡Contraseña actualizada exitosamente!")
                        Control2 = False
                    elif z == 2:
                        print("Excelente!, este es el inventario actual:\n")
                        Funciones_del_código.Imprimir_inventarios(inventarios)
                        v = str(input("¿Qué sección desea modificar?(Mecatos, Aseo, Variedades):"))
                        v = v.capitalize()
                        Control2 = False
                        control3 = True
                        while control3 == True:
                            d = int(input(f"Bien, ¿qué quieres hacer en la sección {v}?(1 para Cambiar el precio de un producto, 2 para Modificar la cantidad en tienda): "))
                            system("cls")
                            if d not in (1,2):
                                print("Por favor selecione una opción correcta")
                                control3 = True
                            elif d == 1:
                                Producto_nuevo = str(input(f"Que producto deseas modificar?(Asegurate que este se encuentre en el inventario actual), copialo tal cual aparece aqui{inventarios[v].keys()}: "))
                                Producto_nuevo1 = float(input(f"\nPerfecto!, ¿Cuál será el nuevo precio de {Producto_nuevo}?: "))
                                system('cls')
                                Funciones_del_código.Modificar_inventarios(inventarios, v, d, Producto_nuevo, Producto_nuevo1)
                                control3 = False
                            elif d == 2:
                                Producto_nuevo = str(input(f"Que producto deseas modificar?(Asegurate que este se encuentre en el inventario actual), copialo tal cual a aparece aqui{inventarios[v].keys()}: "))
                                Producto_nuevo1 =float(input(f"\nPerfecto!, ¿Cuál es la nueva cantidad?:"))
                                system('cls')
                                Funciones_del_código.Modificar_inventarios(inventarios, v, d, Producto_nuevo, Producto_nuevo1)
                                control3 = False




if __name__ == "__main__":
    main()
