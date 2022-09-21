opcion=0
num1=int(input("ingresa un numero 1"))
num2=int(input("ingresa un numero 2"))
while True:
    print("""Opciones:
    1)Suma
    2)Resta
    3)Salir""")
    opcion=int(input("ingresa la operacion a realiar"))
    if opcion == 1:
        print("la suma es: ", num1+num2)
        print("¿Desea realizar otra operacion? s/n")
        rpta=input()
        if rpta=="s":
            continue
    elif opcion == 2:
        print("la resta es : ", num1-num2)
    elif opcion==3:
        print("adios")
        break
