
def main():
    from os import system
    def Congfiguracion_de_admministrador():
        
        pass
    contraseña = "Contraseña_predeterminada123"
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
            cont = str(input("Por favor ingrese su contraseña: "))
            system("cls")
            control = False
            while control == False:
                contador = 0
                if contador <= 3:
                    if cont == contraseña:
                        Control2 = True
                        while Control2 == True:
                            print("Hola Administrador/a, ¿qué deseas hacer?\n 1.Cambiar la contraseña\n 2.Editar los inventarios")
                            z = int(input("Selecciona una opción (1 o 2): "))
                            system("cls")
                            if z not in (1,2):
                                Control2 = True
                            elif z == 1:
                                print(f"Recuerda que la contraseña acutual es: {contraseña!r}")
                                contraseña = str(input("Ingresa la nueva contraseña:")) 
                                print("¡Contraseña actualizada exitosamente!")
                                Control2 = False
                        control = True 
                    else: 
                        contador += 1
                        print(f"Contraseña incorrecta, lleva {contador} intentos de 3 disponibles")
                else:#colocar el código para el
                    pass


if __name__ == "__main__":
    main()
