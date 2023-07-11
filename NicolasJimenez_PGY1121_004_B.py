import numpy as np
"""ordenados = sorted(pasajeros, key=lambda x: x[0], reverse=False)"""

departamentos = []
departamentos_ocupados = []
compradores = []
a = 0
b = 0
c = 0
d = 0
for fila in range(1,11):
    departamentos.append([f"A{fila}", f"B{fila}", f"C{fila}", f"D{fila}"])
departamentos = np.array(departamentos)


def opciones():
    menu_completo = """Selecione una opcion
    1. Comprar departamento
    2. Mostrar departamentos disponibles
    3. Ver listado de compradores
    4. Mostrar ganancias totales
    5. Salir
    """
    while True:
        try:
            opcion = int(input(menu_completo))
            if opcion <= 0 or opcion > 5:
                raise ValueError
            return opcion
        except ValueError:
            print("Opcion incorrecta")


def rut():
    while True:
        try:
            a = int(input("Ingrese su rut, sin punto ni digito verificador: "))
            if len(f"{a}") != 8:
                print("el rut debe tener 8 caracteres ")
                raise ValueError
            break
        except ValueError:
            print("Error al ingresar el rut")
    return a

def comprar():
    global a, b, c, d
    while True:
        try:
            numero = int(input("Ingrese el piso de su departamento: "))
            if numero <= 0 or numero > 10:
                print("ingrese correctamente el numero del departamento")
                raise ValueError
            break
        except ValueError:
            print("error al ingresar dato")
    while True:
        print("""Tipo A, 3.800 UF\nTipo B, 3.000 UF\nTipo C, 2.800 UF\nTipo D, 3.500 UF""")
        letra = input("Ingrese la letra de su departamento: ").upper()
        if letra != "A" and letra !="B" and letra !="C" and letra !="D":
            print("Ingrese una letra entre A, B, C, D")
        else: 
            break
    numero = str(numero)
    departamento = letra + numero
    if departamento in departamentos_ocupados:
        print("Departamento No Disponible, intente con otra opcion")
        return
    else:
        print("departamento disponible")
        departamentos_ocupados.append(departamento)
        filas, columnas = np.where(departamentos == departamento)
        departamentos[filas, columnas] = "X"
        if letra == "A":
            a += 1
        elif letra == "B":
            b += 1
        elif letra == "C":
            c += 1
        elif letra == "D":
            d += 1
    cliente = rut()
    compradores.append([cliente,departamento])
    return print("Cliente agregado exitosamente")
    

def verdepa():
    i = 1
    print("   A, B, C, D")
    for fila in departamentos:
        print(f"{i}", end=".")
        for elemento in fila:
            if elemento == "X":
                print("x", end=" ")
            else:
                print(end=" ")
        print()
        i += 1


def comprador():
    ordenados = sorted(compradores, key=lambda x: x[0], reverse=False)
    for cliente in ordenados:
        print(cliente[0], cliente[1])


def ventas():
    global a, b, c, d
    menu_ventas = f"""Tipo de departamento Cantidad Total
Tipo A, 3.800 UF {a} ${a*3800} UF
Tipo B, 3.000 UF {b} ${b*3000} UF
Tipo C, 2.800 UF {c} ${c*2800} UF
Tipo D, 3.500 UF {d} ${d*3500} UF
Total            {a+b+c+d} ${a*3800+b*3000+c*2800+d*3500} UF"""
    print(menu_ventas)


def main():
    while True:
        menu = opciones()
        if menu == 1:
            comprar()
        elif menu == 2:
            verdepa()
        elif menu == 3:
            comprador()
        elif menu == 4:
            ventas()
        elif menu == 5:
            print("Gracias por usar la App")
            exit()


if __name__ == "__main__":
    main()

#Git code: https://github.com/Niko2Tech/Duocuc