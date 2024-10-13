
def main():
    from os import system
    import time
    import Funciones_del_código
    contraseña = "123"
    control = True
    while control == True:
        lista1 = [1, 2]
        print("1. Cliente\n2.Administrador")
        a = int(input(f"Por favor seleccione su rol (1 o 2): "))
        system("cls")
        if a not in lista1:
            print("Por favor seleccione una opción correcta")
        elif a == 1:
            print()
            control = False
        elif a == 2:
            system("cls")
            control = False
            control1 = False 
            while control1 == False:
                cont = str(input("Por favor ingrese su contraseña: "))
                system("cls")
                if cont != contraseña:
                    print("Contraseña incorrecta, intetalo nuevamente dentro de ")
                    Tiempo_bloqueo = Funciones_del_código.Bloqueo_de_seguridad(10)    
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
                            print("Excelente!, este es el inventario actual:")
                            Funciones_del_código.Imprimir_inventarios(Funciones_del_código.inventarios)
                            v = str(input("¿Qué sección desea modificar?(Mecatos, Aseo, Variedades):"))
                            v = v.capitalize()
                            control3 = True
                            while control3 == True:
                                d = int(input(f"Bien, ¿qué quieres hacer en la sección {v}?(1 para Cambiar el precio de un producto, 2 para Modificar la cantidad en tienda): "))
                                system("cls")
                                if d not in (1,2):
                                    print("Por favor selecione una opción correcta")
                                    control3 = True
                                elif d == 1:
                                    Producto_nuevo = str(input("Que producto deseas modificar?(Asegurate que este se encuentre en el inventario actual): "))
                                    Producto_nuevo1 = int(input(f"\nPerfecto!, ¿Cuál será el nuevo precio de {Producto_nuevo}?: "))
                                    system('cls')
                                    print("\nEste es el nuevo inventario:\n")
                                    Funciones_del_código.Modificar_inventarios(Funciones_del_código.inventarios, v, d, Producto_nuevo, Producto_nuevo1)
                                    control3 = False
                                elif d == 2:
                                    Producto_nuevo = str(input("Que producto deseas modificar?(Asegurate que este se encuentre en el inventario actual): "))
                                    Producto_nuevo1 =int(input(f"\nPerfecto!, ¿Cuál es la nueva cantidad?:"))
                                    system('cls')
                                    print("\nEste es el nuevo inventario:\n")
                                    Funciones_del_código.Modificar_inventarios(Funciones_del_código.inventarios, v, d, Producto_nuevo, Producto_nuevo1)
                                    control3 = False

                            Control2 = False
                    control1 = True



if __name__ == "__main__":
    main()
