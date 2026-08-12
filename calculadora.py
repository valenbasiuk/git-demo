# Calculadora sencilla

print("calculadora sencilla")
print("operaciones: +, -, *, /")

while True:
    try:
        num1 = float(input("ingrese el primer número: "))
        operacion = input("ingrese la operación (+, -, *, /): ")
        num2 = float(input("ingrese el segundo número: "))

        if operacion == "+":
            resultado = num1 + num2
        elif operacion == "-":
            resultado = num1 - num2
        elif operacion == "*":
            resultado = num1 * num2
        elif operacion == "/":
            if num2 == 0:
                print("no se puede dividir por cero.")
                continue
            resultado = num1 / num2
        else:
            print("operación inválida.")
            continue

        print(f"resultado: {resultado}")

    except ValueError:
        print("entrada inválida. intente de nuevo.")

    opcion = input("¿desea realizar otra operacion? (s/n): ").lower()
    if opcion != "s":
        print("chao!")
        break
