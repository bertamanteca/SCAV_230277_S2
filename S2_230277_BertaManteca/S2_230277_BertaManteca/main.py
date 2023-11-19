def main():
    print("¿Qué ejercicio quieres ejecutar?")
    print("1. Ex1")
    print("2. Ex2")
    print("3. Ex3")
    print("4. Ex4")
    print("5. Ex5")
    print("6. Ex6")

    ejercicio_elegido = input("Introduce el número del ejercicio: ")

    if ejercicio_elegido == '1':
        import ex1
        ex1.ejecutar()
    elif ejercicio_elegido == '2':
        import ex2
        ex2.ejecutar()
    elif ejercicio_elegido == '3':
        import ex3
        ex3.ejecutar()
    elif ejercicio_elegido == '4':
        import ex4
        ex4.ejecutar()
    elif ejercicio_elegido == '5':
        import ex5
        ex5.ejecutar()
    elif ejercicio_elegido == '6':
        import ex6
        ex6.ejecutar()
    else:
        print("Número de ejercicio no válido. Introduce un número del 1 al 6.")

if __name__ == "__main__":
    main()
