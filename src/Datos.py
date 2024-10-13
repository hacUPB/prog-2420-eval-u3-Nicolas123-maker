
def main():
    from os import system
    import time
    from src.Funciones_del_código import Bloqueo_de_seguridad
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
            control = False
            control1 = False 
            while control1 == False:
                cont = str(input("Por favor ingrese su contraseña: "))
                system("cls")
                if cont != contraseña:
                    print("Contraseña incorrecta, intetalo nuevamente dentro de ")
                    Tiempo_bloqueo = Bloqueo_de_seguridad(10)    
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
                            pass 
                    control1 = True



if __name__ == "__main__":
    main()
