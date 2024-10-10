
def main():
    def Congfiguracion_de_admministrador():
        
        pass
    control = True
    while control == True:
        lista1 = [1, 2]
        print("1. Cliente\n2.Administrador")
        a = int(input(f"Por favor seleccione su rol: "))
        if a not in lista1:
            print("Por favor seleccione una opción correcta")
        elif a == 1:
            print()
            control = False
        elif a == 2:
            cont = str(input("Por favor ingrese su contraseña: "))
            if cont == contraseña:
                
            control = False


         


if __name__ == "__main__":
    main()
