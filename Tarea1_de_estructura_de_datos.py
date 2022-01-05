#Nombre: Jairo Calle
#Carrera: Ingeniería en software 3er nivel

class deber:
    # ¿De cuál tipo de dato sería la variable donde almacena lo siguiente?
    def ejercicio1(self):
        variable1 = "Hola mundo"
        variable2 = "True"
        variable3 = ",,1'"
        variable4 = ",,c'"
        variable5 = 256
        variable6 = 8 > 19
        print("La variable 1 es de tipo: ", type(variable1))
        print("La variable 2 es de tipo: ", type(variable2))
        print("La variable 3 es de tipo: ", type(variable3))
        print("La variable 4 es de tipo: ", type(variable4))
        print("La variable 5 es de tipo: ", type(variable5))
        print("La variable 6 es de tipo: ", type(variable6))
    # ¿Siguiendo la prioridad de operadores, convierta a expresión matemática,

    # resuelva e indique en cuál tipo de variable almacenará el resultado de las
    # siguientes expresiones:
    def ejercicio2(self):
        operacion1 = (5 + 3 * 2) + 9 > 3 * 5 * 14 % 3
        operacion2 = 2 * (4 - 10 + 8) / 2 * 36 * (1 / 2)
        operacion3 = 260 / 12 + 54 % 3 - 85 % 7
        operacion4 = (48 < 2 * 3) or (2 * 7 < 12)
        operacion5 = ((8 > 2) or (932 < 23)) and (4 == 2)
        print("El resultado de la operacion 1 es de tipo booleano: " + str(operacion1))
        print("El resultado de la operacion 2 es de tipo flotante: " + str(operacion2))
        print("El resultado de la operacion 3 es de tipo flotante: " + str(operacion3))
        print("El resultado de la operacion 4 es de tipo booleano: " + str(operacion4))
        print("El resultado de la operacion 5 es de tipo booleano: " + str(operacion5))

    # Dados dos (2) números calcule la suma, resta, multiplicación, división y módulo.

    def ejercicio3(self):
        numero1 = int(input("Ingrese el numero 1: "))
        numero2 = int(input("Ingrese el numero 2: "))
        suma = numero1 + numero2
        resta = numero1 - numero2
        multiplicacion = numero1 * numero2
        division = numero1 / numero2
        modulo = numero1 % numero2
        print("El resultado de la suma es: " + str(suma))
        print("El resultado de la resta es: " + str(resta))
        print("El resultado de la multiplicacion es: " + str(multiplicacion))
        print("El resultado de la division es: " + str(division))
        print("El resultado del modulo es: " + str(modulo))

    # Dados tres (3) números, Hacer una aplicación que calcule la resolvente.
    def ejercicio4(self):
        import math
        print("ax² + bx + c = 0\n")
        a, b, c = [float(input(f"Ingrese el coeficiente {coef}: ")) for coef in ("a", "b", "c")]
        discriminante = b * b - 4 * a * c
        if discriminante < 0:
            print(f"La ecuación no tiene soluciones reales.")
        else:
            raiz = math.sqrt(discriminante)
            x1 = (-b + raiz) / (2 * a)
            if discriminante != 0:
                x2 = (-b - raiz) / (2 * a)
                print(f"Las soluciones son: {x1} y {x2}.")
            else:
                print(f"La única solución es: x = {x1}")

    # Dados dos (2) lados de un triángulo en cm, calcular la hipotenusa del mismo.

    def ejercicio5(self):
        A = int(input("Ingrese el  valor del primer lado: "))
        B = int(input("Ingrese el  valor del segundo lado: "))
        hipotenusa = (A ** + B ** 2) ** 0.5
        print("El valor de la hipotenusa es: " + str(hipotenusa))

    # Dado un (1) número, imprimir 0 si es par y 1 si es impar.
    def ejercicio6(self):
        num = int(input("Ingresa un número: "))
        if num % 2 == 0:
            print("El numero es par")
        else:
            print("El numero es impar")

    # Dado un (1) número binario de cuatro (4) dígitos imprimir su bit da paridad.
    # El bit de paridad es 1 si el número de bits 1 es impar y 0 en caso contrario.
    def ejercicio7(self):
        a = int(input("Introduce el año: "))
        if a % 4 == 0 and a % 100 != 0 or a % 400 == 0:
            print(a, " es un año bisiesto")
        else:
            print(a, " no es un año bisiesto")

    # Dado un (1) número binario de cuatro (4) dígitos imprimir su valor.
    def ejercicio8(self):
        numero_binario = input("Ingrese un numero binario de cuatro digitos: ")
        numero_decimal = 0
        for posicion, digito_string in enumerate(numero_binario[::-1]):
            numero_decimal += int(digito_string) * 2 ** posicion
        print("El valor del numero binario es: " + str(numero_decimal))

    # Dado un (1) número de cuatro (4) dígitos imprimirlo por separado en unidades,
    # decenas, centenas y unidades de mil.
    def ejercicio9(self):
        numero = int(input("ingrese el numero: "))
        unidades = numero % 10
        decenas = (numero % 100 - numero % 10) // 10
        centenas = (numero % 1000 - numero % 100) // 100
        unidadesdemil = (numero % 10000 - numero % 1000) // 1000
        print("unidades: " + str(unidades))
        print("decenas: " + str(decenas))
        print("centenas: " + str(centenas))
        print("unidades de mil: " + str(unidadesdemil))

    # Todos los años que se dividen exactamente entre 400, o que son divisibles
    # exactamente entre 4 y no son divisibles exactamente entre 100 son años bisiestos.
    # Usando estas premisas crea un algoritmo que lea una fecha como un número
    # entero con el formato ddmmaaaa, y luego extraiga el año de la fecha indicando si
    # el mismo es un año bisiesto o no.
    def ejercicio10(self):
        print("Ingrese una fecha en dd mm aaaa (separados con espacio): ", end=" ")
        d, m, a = map(int, input().split())
        print("\nla fecha que pusiste es: {}/{}/{}".format(d, m, a))

        if a % 400 == 0:
            print("el año {} SI es bisiesto".format(a))
        elif a % 100 == 0:
            print("el año {} NO es bisiesto".format(a))
        elif a % 4 == 0:
            print("el año {} SI es bisiesto".format(a))
        else:
            print("el año {} NO es bisiesto".format(a))

    # Dado un número entero cuya cantidad de dígitos es igual a 5, determine
    # si es capicúa.
    # Nota: un número capicúa es aquel que se lee igual hacia adelante que hacia atrás
    def ejercicio11(self):
        n = int(input("Ingresa un número de 5 dígitos: "))
        s = str(n)
        reverso = s[::-1]
        if s == reverso:
            print("SI es capicua")
        else:
            print("NO es capicua")

    # Cree un algoritmo que tome por entrada las horas y minutos de un día y dé como

    # resultado su equivalente en segundos.
    def ejercicio12(self):
        print("Ingrese una hora y minutos en hh mm (separados con espacio): ", end=" ")
        h, m = map(int, input().split())
        s = (h * 3600) + (m * 60)
        print("las horas y minutos es: {} hora(s):{} minuto(s)".format(h, m))
        print("\nllevadas a SEGUNDOS es: {} segundos".format(s))

    # Para un valor entero positivo que representa una cantidad en segundos, indicar
    # su equivalente en minutos, horas y días.
    def ejercicio13(self):
        seg = int(input("Ingrese los segundos que desee convertir: "))
        if seg >= 60:
            min = seg / 60
            print("\n en MINUTOS: {} minuto(seg)".format(min))
        else:
            print("\n en MINUTOS: 0 minuto(seg)")
        if seg >= 3600:
            hor = seg / 3600
            print("\n en HORAS: {} hora(seg)".format(hor))
        else:
            print("\n en HORAS: 0 dia(seg)")
        if seg >= 86400:
            dia = seg / 86400
            print("\n en DIAS: {} dia(seg)".format(dia))
        else:
            print("\n en DIAS: 0 dia(seg)")

    # Dados tres números enteros positivos A, B y C, determine ¿cuál de ellos es el
    # mayor? y ¿cuál es el segundo mayor?
    def ejercicio14(self):
        n1 = int(input("ingrese el primer número positivo: "))
        n2 = int(input("ingrese el segundo número positivo: "))
        n3 = int(input("ingrese el tercer número positivo: "))
        if n3 > n2 > n1:
            print("\n el número mayor es: {} y el segundo mayor es {} ".format(n3, n2))
        elif n3 > n1 > n2:
            print("\n el número mayor es: {} y el segundo mayor es {} ".format(n3, n1))
        elif n2 > n3 > n1:
            print("\n el número mayor es: {} y el segundo mayor es {} ".format(n2, n3))
        elif n2 > n1 > n3:
            print("\n el número mayor es: {} y el segundo mayor es {} ".format(n2, n1))
        elif n1 > n2 > n3:
            print("\n el número mayor es: {} y el segundo mayor es {} ".format(n1, n2))
        elif n1 > n3 > n2:
            print("\n el número mayor es: {} y el segundo mayor es {} ".format(n1, n3))

    # En un estacionamiento el monto a pagar se calcula multiplicando el número de
    # horas que permaneció el automóvil dentro del estacionamiento por Bs. 4 y se
    # incrementa esta cantidad en Bs. 2,50 por cada media hora adicional.
    # Ahora se desea que usted elabore un algoritmo que a partir de la hora de entrada
    # y la hora de salida de un vehículo (las mismas corresponden a un mismo día)
    # calcule el monto a pagar por el dueño del vehículo.
    # La entrada vendrá dada por dos enteros positivos el primero representa las horas
    # y el segundo los minutos, además por último se debe leer un carácter (A o P) que
    # indica si la hora es AM o PM.
    def ejercicio15(self):
        t1 = [0, 0, "", 0, 0, ""]
        t2 = [0] * 2
        pbs = ["la hora de entrada", "los minutos excedentes de entrada", 2, "la hora de salida",
                   "los minutos excedentes de salida", 5]
        ct = 0

        for i in pbs:
            if (ct != 2 or ct != 5):
                if (i != 2 and i != 5):
                    t1[ct] = int(input("Ingrese {}: ".format(i)))
                ct += 1
            if ct == 2 or ct == 5:
                a = input("La hora que ingresó es AM o PM? ")
                t1[(pbs[ct])] = a

        t2[0] = (t1[0] * 3600) + (t1[1] * 60)
        t2[1] = (t1[3] * 3600) + (t1[4] * 60)

        if t1[2] == t1[5]:
            nhp = t2[1] - t2[0]
        else:
            nhp = (43200 - t2[0]) + t2[1]

        t2[0] = (nhp - (nhp % 3600)) / 3600
        t2[1] = (nhp % 3600) / 60
        print(t2)
        mp = t2[0] * 4

        if t2[1] >= 30:
            mp = mp + 2.50
        print("El dueño del vehículo pagará Bs. ", mp)

    # El IMC resulta de la división de la masa del individuo (en kilogramos) entre el
    # cuadrado de la estatura (en metros). El índice de masa corporal es un indicador
    # del peso de una persona en relación con su altura.
    # Clasificación del IMC de acuerdo con la OMS de la ONU:
    # a. Menor a 16: Criterio de ingreso.
    # b. 16 a 16.9: infra peso.
    # c. 17 a 18.4: bajo peso.
    # d. 18.5 a 24.9: peso normal.
    # e. 25 a 29.9: sobrepeso.
    # f. 30 a 34.9: obesidad pre-mórbida.
    # g. 40 a 45: obesidad mórbida.
    # h. Mayor a 45: obesidad híper-mórbida.
    def ejercicio16(self):
        print("\n")
        masa = float(input("Ingrese la masa en kilogramos: "))
        estatura = float(input("Ingrese su estatura en metros: "))
        IMC = masa / estatura
        if 16 < IMC < 16.9:
            print("Infra peso")
        elif 17 < IMC < 18.4:
            print("Bajo peso")
        elif 18.5 < IMC < 24.9:
            print("Peso normal")
        elif 25 < IMC < 29.9:
            print("Sobrepeso")
        elif 30 < IMC < 34.9:
            print("Obesidad pre-móbida")
        elif 40 < IMC < 45:
            print("Obesidad mórbida")
        else:
            print("Obesidad híper-móbida ")

    # Escriba un algoritmo que reciba una fecha (día y mes) correspondiente al año
    # 2014 e imprima por pantalla el número de días que han pasado desde el 1 de
    # Enero de 2014 hasta la fecha dada.
    def ejercicio17(self):
        año = int(input("Ingrese el año: "))
        mes = int(input("Ingrese el mes: "))
        dia = int(input("Ingrese el dia: "))
        from datetime import date
        fechainicial = date(2014, 1, 1)
        fechafinal = date(año, mes, dia)
        dias = fechafinal - fechainicial
        print("El numero de dias es de: " + str(dias))

    # Solicitar un número entre el 1 y el 12 e imprimir el mes correspondiente a dicho
    # número.
    def ejercicio18(self):
        n = int(input("Ingrese el numero del mes 1-12 : "))
        if n == 1:
            print("enero")
        elif n == 2:
            print("febrero")
        elif n == 3:
            print("marzo")
        elif n == 4:
            print("abril")
        elif n == 5:
            print("mayo")
        elif n == 6:
            print("junio")
        elif n == 7:
            print("julio")
        elif n == 8:
            print("agosto")
        elif n == 9:
            print("septiembre")
        elif n == 10:
            print("octubre")
        elif n == 11:
            print("noviembre")
        elif n == 12:
            print("diciembre")
        else:
            print("El numero no se encuentra en el rango establecido")

    # En un almacén se hace un 20% de descuento a los clientes cuya compra supere

    # los Bs 1000, se desea que realice un algoritmo el cual tome por entrada el monto
    # a pagar por el cliente y arroje como salida el monto aplicando el descuento de
    # ser necesario.
    def ejercicio19(self):
        print("Ingrese Monto : ")
        monto = float(input())
        if monto > 1000:
            print("Tendrá un Descuento del 20% : ", monto * 0.20)
        else:
            print("El monto no es mayor que 1000 , por lo tanto o hay descuento")

    # Dado un número entero N, calcular e informar al usuario cuántos dígitos tiene
    # dicho número.
    def ejercicio20(self):
        n = int(input("ingrese un numero: "))
        contador = len(str(n))
        print("El numero ingresado tiene %s digitos" % (contador))

    # Dado un número, determine si es capicúa.
    # Nota: un número capicúa es aquel que se lee igual hacia adelante que hacia atrás.
    def ejercicio21(self):
        n = int(input("Ingresa un número: "))
        s = str(n)
        reverso = s[::-1]
        if s == reverso:
            print("SI es capicua")
        else:
            print("NO es capicua")

    # Dado un número N determinar si es un número primo.
    # Nota: Un número primo es aquel que solo es divisible por 1(uno) y por el mismo.
    def ejercicio22(self):
        numero = int(input("Ingrese un numero: "))
        antecesor = numero - 1
        residuo = 0
        contadorDivisibles = 0
        while antecesor > 1:
            residuo = numero % antecesor
            if residuo == 0:
                contadorDivisibles = contadorDivisibles + 1
            antecesor = antecesor - 1
        if contadorDivisibles == 0:
                print("El numero ingresado es primo")
        else:
                print("El numero no es primo")

    # Construya un programa que dado un valor entero N, haga el cálculo de la función

    # factorial utilizando iterativas.
    def ejercicio23(self):
        numero = int(input("ingrese numero: "))
        factorial = 1
        if numero != 0:
            for i in range(1, numero + 1):
                factorial = factorial * i
        print("El factorial:", factorial)

    # Dado un número entero N que representa una contraseña y asumiendo que una
    # contraseña debe tener al menos 10 dígitos para ser segura, determine si la
    # contraseña ingresada por el usuario es correcta, de no serlo debe pedirla
    # nuevamente hasta que tenga los 10 (diez) dígitos solicitados y al ser correcta
    # mostrar un mensaje de éxito al usuario, por salida estándar.
    def ejercicio24(self):
        validacion = False
        while validacion == False:
            clave = input("Ingrese su contraseña: ")
            if len(clave) == 10:
                print("Ingreso de contraseña exitoso!")
                validacion = True
            else:
                print("La contraseña no es segura, vuelva a intentar!")
                validacion = False

    # Dada una secuencia de números terminada en cero (0), elaborar un algoritmo que
    # informe al usuario qué valor tiene el número mayor y qué valor tiene el número
    # menor, sin contar el cero (0).
    def ejercicio25(self):
        lista = []
        a = True
        while a:
            num = int(input("Ingresar un numero(ingrese el 0 si desea terminar)"))
            if num == 0:
                a = False
            else:
                lista.append(num)
        mayor, menor = deber.mayor_menor(lista)
        if len(lista) > 0:
            print("El numero mayor es:", mayor)
            print("El numero menor es:", menor)

    def mayor_menor(lista):
        mayor = 0
        menor = 9999999999999999999999
        for num in lista:
            if num > mayor:
                mayor = num

            if num < menor:
                menor = num
        return mayor, menor

    # Se tiene una secuencia de enteros terminada en cero, que corresponde a la edad,
    # peso y estatura de una muestra de hombres y mujeres mayores de 18 años. Con
    # base en dicha secuencia se desea realizar un estudio a fin de conocer:
    #  Edad promedio de todas las personas en la muestra.
    #  Peso promedio de todas las personas en la muestra.
    #  Estatura promedio de todas las personas en la muestra.
    #  Cuántas personas hay con edad entre los 18 y 25 años.
    #  Cuántas personas son mayores a 36 años.
    #  Cuál es el promedio de peso de las personas con edades entre 18 y 35 años.
    def ejercicio26(self):
        edad = [20, 18, 32, 19, 22, 40]
        peso = [42, 52, 49, 47, 50, 46]
        estatura = [1.45, 1.63, 1.52, 1.70, 1.68, 1.57]
        prom_edad = (sum(edad)) / len(edad)
        prom_peso = (sum(peso)) / len(peso)
        prom_estatura = (sum(peso)) / len(estatura)
        c = 0
        x = 0
        while c < 8:
            x += (edad.count(18 + c))
            c += 1
        c = 1
        TreSeis = 0
        while c < 150:
            TreSeis += (edad.count(36 + c))
            c += 1
        c = 0
        contPos = 0
        while c < 36:
            contPos = [i for i, x in enumerate(edad) if x >= 18 and x <= 35]
            c += 1
        suma = 0
        c = 0
        while c < len(contPos):
            suma += peso[contPos[0 + c]]
            c += 1
        print(f"El promedio de edades de todas las personas es de: {prom_edad:.2f}")
        print(f"El promedio de peso de todas las personas es de: {prom_peso:.2f}")
        print(f"El promdedio de estatura de todas las personas es de: {prom_estatura:.2f}")
        print(f"Hay {x}, personas con edad de entre [18-25] ")
        print(f"Hay {TreSeis}, personas mayor(es) a 36 años")
        print(f"El promedio de peso entre las personas de 18 a 35 años es: {suma / len(contPos):.2f}")

    # Construye un algoritmo que calcule e imprima la tabla de multiplicar, desde la
    # tabla del 1 hasta la del 10.
    def ejercicio27(self):
        numero = int(input("Ingrese un numero: "))
        for i in range(1, 11):
            print(f' {i} x {numero}={i * numero}')

    # Escribir un algoritmo que muestre todas las fichas de dominó, sin repetir.
    def ejercicio28(self):
        for i in range(1, 7):
            for j in range(i, 7):
                print("todas las fichas de domino {}:{}".format(i, j))

    # Dados N número positivos (N>1) calcular el promedio de esta serie. Considere que
    # la serie termina al leer un 0.
    def ejercicio29(self):
        contador = 0
        suma = 0
        numero = 1
        while numero != 0:
            numero = int(input("ingrese un numero entero (0 para terminar):"))
            if numero != 0:
                suma += numero
                contador += 1
        if contador == 0:
            print("no digito ningun numero.")
        else:
            promedio = suma / contador
            print("El promedio de los {} numero es igual a {}.".format(contador, promedio))

    # Construya una función que solicite edades al usuario y determine el promedio de
    # las edades mayores a 18 años. El usuario indicará cuando desea dejar de
    # suministrar datos de entrada. En la Acción Principal se informará el promedio
    # calculado.
    def ejercicio30(self):
        acumulador = int(0)
        for x in range(1, 5):
            edad = int(input("ingrese la edad: "))
            acumulador = acumulador + edad
        print("El promedio de las edades es de: ", str(acumulador / 5))
    # Construya una función “Eleva” Que reciba como parámetros una base y un exponente
    # y retorne al algoritmo principal el resultado de elevar un numero al otro
    def ejercicio31(self):
        base = int(input("Ingrese la base: "))
        exponente = int(input("Ingrese el exponente: "))
        potencia = base ** exponente
        print(str(base) + "^" + str(exponente) + " es igual a: ", potencia)


    # Escriba una función que calcule el perímetro del pentágono (siendo el perímetro
    # la suma de los lados del polígono).
    def ejercicio32(self):
        lados = int(input("Ingrese el valor de los lados del pentagono: "))
        Perimetro = lados * 5
        print("El perimetro del pentagono es: " + str(Perimetro))


    # Escriba una acción (MillasAKilometros) que convierta una distancia en millas a
    # kilómetros (1milla = 1.60935km). Esta acción recibirá como parámetros: el nombre
    # de la ciudad origen, el nombre de la ciudad destino y la distancia en millas
    # entre ellas y debe retornar la distancia entre las ciudades en kilómetros.
    # Desarrolle además una acción principal en donde utilice a la acción
    # MillasAKilometros para convertir e informar la distancia en kilómetros entre 4
    # pares de ciudades suministradas por el usuario.
    def ejercicio33(self):
       ciudad_A = input("Ingrese el nombre de la ciudad de origen: ")
       ciudad_B = input("Ingrese el nombre de la ciudad de destino: ")
       distancia = int(input("Ingrese la distancia en millas que hay entre las dos ciudades: "))
       km = distancia * 1.60935
       print("La distancia en km que hay entre", ciudad_A, "y", ciudad_B, "es de", km)


tarea = deber()
tarea.ejercicio1()
tarea.ejercicio2()
tarea.ejercicio3()
tarea.ejercicio4()
tarea.ejercicio5()
tarea.ejercicio6()
tarea.ejercicio7()
tarea.ejercicio8()
tarea.ejercicio9()
tarea.ejercicio10()
tarea.ejercicio11()
tarea.ejercicio12()
tarea.ejercicio13()
tarea.ejercicio14()
tarea.ejercicio15()
tarea.ejercicio16()
tarea.ejercicio17()
tarea.ejercicio18()
tarea.ejercicio19()
tarea.ejercicio20()
tarea.ejercicio21()
tarea.ejercicio22()
tarea.ejercicio23()
tarea.ejercicio24()
tarea.ejercicio25()
tarea.ejercicio26()
tarea.ejercicio27()
tarea.ejercicio28()
tarea.ejercicio29()
tarea.ejercicio30()
tarea.ejercicio31()
tarea.ejercicio32()
tarea.ejercicio33()











































