from random import randint


lst_alumnos = []

def pregunta():
    menu = """ingrese una de las siguientes opciones indicando su numero:
    1) Ingresar alumno
    2) Buscar alumno
    3) Imprimir Certificado
    4) Salir
    """
    while True:
        try:
            numero = int(input(menu))
            if numero < 1 or numero > 4:
                raise ValueError
            return numero
        except ValueError:
            print("ingrese una opcion valida")


def validar_dato(parametro):
    dato = input(f"ingrese {parametro}: ")
    if dato == "":
        print("el dato no puede estar vacio intente nuevamente")
        validar_dato(parametro)
    elif parametro == "rut":
        if len(dato) != 10:
            print("El rut debe tener 10 caracteres intente nuevamente")
            validar_dato(parametro)
        elif len(dato) == 10:
            print("rut ingresado correctamente")
            return dato
    elif parametro == "carrera":
        print("carrera agregada correctamente")
        return dato
    elif parametro != "rut":
        if parametro == "fecha de nacimiento":
            print("fecha de nacimiento agregada correctamente")
            return dato
        if len(dato) <= 2 or len(dato) >= 12:
            print(f"El {parametro} debe estar dentro de 2 a 12 caracteres")
            validar_dato(parametro)
        else:
            print(f"{parametro} agregado correctamente")
            return dato


def asignaturas():
    asignatura = []
    while True:
        nombre_a = input("ingrese el nombre de la asignatura (debe ingresar al menos una asignatura y un promedio): ")
        if nombre_a == "":
            print("el nombre no puede estar vacio")
            asignaturas()
        while True:
            nota = float(input("Ingrese el promedio: "))
            if nota < 1 or nota > 7:
                print("El promedio debe ser entre 1.0 y 7.0 ")

            else:
                asignatura.append([nombre_a, nota])
                print("datos agregados correctamente")
                while True:
                    salida = input("si desea salir coloque S, en caso de continuar coloque C: ")
                    if salida == "s" or salida == "S":
                        return asignatura
                    elif salida == "c" or salida == "C":
                        break
                    else:
                        print("Elija una de las opciones")
                break
        
        

def grabar():
    print("Debe ingresar los siguientes datos")
    rut = validar_dato("rut")
    nombre = validar_dato("nombre")
    apellido = validar_dato("apellido")
    fecha = validar_dato("fecha de nacimiento")
    carrera = validar_dato("carrera")
    asignatura = asignaturas()
    lst_alumnos.append([rut, nombre, apellido, fecha, carrera, asignatura])
    print("alumno agregado correctamente")


def buscar():
    if len(lst_alumnos) == 0:
        print("no existen alumnos para buscar")
    else:
        rut = validar_dato("rut")
        for alumno in lst_alumnos:
            if alumno[0] == rut:
                print(f"rut: {alumno[0]}")
                print(f"nombre: {alumno[1]}")
                print(f"apellido: {alumno[2]}")
                print(f"fecha de nacimiento: {alumno[3]}")
                print(f"carrera: {alumno[4]}")
                print(f"asignaturas y promedio: {alumno[5]}")
                return
        print("alumno no encontrado")        


def certificado():
    if len(lst_alumnos) == 0:
        print("no existen alumnos")
        return
    menu = f"""Ingrese el certificado que desea obtener indicando su numero
    1) Alumno Regurar ${randint(1000,5000)}
    2) Concentracion de notas ${randint(1000,5000)}
    3) Certificado de matricula ${randint(1000,5000)}
    """
    rut = validar_dato("rut")
    alumno2 = ""
    for alumno in lst_alumnos:
            if alumno[0] == rut:
                rut = alumno[0]
                nombre = alumno[1]
                apellido = alumno[2]
                carrera = alumno[4]
                notas = alumno[5]
                alumno2 = "encontrado"
    if alumno2 != "encontrado":
        print("alumno no encontrado")
        return
    while True:
        try:
            numero = int(input(menu))
            if numero < 1 or numero > 3:
                raise ValueError
            if numero == 1:
                print(f"""Certificado alumno regular
                {rut}
                {nombre} {apellido}
                {carrera}""")
                return
            elif numero == 2:
                print(f"""Certificado alumno regular
                {rut}
                {nombre} {apellido}
                {carrera}
                Asignaturas y promedios
                {notas}""")
                return
            elif numero == 3:
                print(f"""Certificado de matricula
                {rut}
                {nombre} {apellido}
                {carrera}""")
                return
        except ValueError:
            print("ingrese una opcion valida")




def salir():
    print("Gracias por usar la aplicacion.\nAutor: Nicolas Jimenez")
    exit()


def main():
    while True:
        opcion = pregunta()
        if opcion == 1:
            grabar()
        elif opcion == 2:
            buscar()
        elif opcion == 3:
            certificado()
        elif opcion == 4:
            salir()


if __name__ == "__main__":
    main()