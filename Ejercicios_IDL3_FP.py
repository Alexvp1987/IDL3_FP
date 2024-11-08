#Ejercicio-01: 
#Se requiere algoritmo para imprimir en pantalla 10 veces el texto “HolaMundo”.

import streamlit as st

st.title("Ejercicios para el IDL3")
st.subheader("Ejercicio 1: Imprimir en pantalla 10 veces el texto HolaMundo")

for i in range(10):
    st.write("HolaMundo")

st.write("********************************************************************************************")

#Ejercicio-02: 
#Se requiere algoritmo para imprimir en pantalla los 10 primeros numeros”.

st.subheader("Ejercicio 2: Imprimir en pantalla los 10 primeros numeros")

for i in range(10):
    st.write(i)

st.write("********************************************************************************************")

#Ejercicio-03:
#Se requiere algoritmo para imprimir la tabla de multiplicar de 1 al 12 con el valor ingresado
#por el usuario

st.subheader("Ejercicio 3: Imprimir tabla multiplicar de 1 al 12")

# Solicitar al usuario que ingrese un número
numero = st.number_input("Ingrese un número para ver su tabla de multiplicar:", min_value=1)

# Imprimir la tabla de multiplicar del número ingresado
for i in range(1, 13):
    resultado = numero * i
    st.write(f"{numero} x {i} = {resultado}")

st.write("********************************************************************************************")


#Ejercicio-04:
#Imprimir la siguiente serie (x+1)+(x+3)+(x+5)+…+(x+100) y su resultado.

st.subheader("Ejercicio 4: Imprimir la siguiente serie (x+1)+(x+3)+(x+5)+…+(x+100) y su resultado.")

x = st.number_input("Ingrese el valor de x:", min_value=1)

# Inicializar la suma
suma = 0

# Calcular la suma de la serie
for i in range(1, 101, 2):  
    suma += (x + i)

# Imprimir la serie
serie = " + ".join(f"({x}+{i})" for i in range(1, 101, 2))
st.write(f"Serie: {serie}")

# Imprimir el resultado
st.write(f"Resultado de la serie: {suma}")

st.write("********************************************************************************************")





#Ejercicio-05:
#Realice un algoritmo para generar e imprimir los números pares que se encuentran entre 0 y 100

st.subheader("Ejercicio 5: Imprimir los numeros pares entre 0 y 100")

# Generar e imprimir números pares entre 0 y 100
for i in range(0, 101, 2):
    st.write(i)

st.write("********************************************************************************************")



#Ejercicio-06:
#Realice un algoritmo para calcular y mostrar la suma de los números pares comprendidos entre 20 y 400.

st.subheader("Ejercicio 6: Mostrar la suma de los numeros pares entre 20 y 400")

suma = 0
# Calcular la suma de los números pares entre 20 y 400
for i in range(20, 401, 2):  # Comienza en 20, termina en 400, incrementa de 2 en 2
    suma += i
# Imprimir el resultado
st.write(f"La suma de los números pares entre 20 y 400 es: {suma}")


st.write("********************************************************************************************")



#Ejercicio-07:
#Realice un algoritmo para calcular y mostrar el promedio de los números pares comprendidos entre 20 y 400


st.subheader("Ejercicio 7: Mostrar el promedio de los numeros pares entre 20 y 400")

# Inicializar la suma y el contador
suma = 0
contador = 0

# Calcular la suma de los números pares entre 20 y 400
for i in range(20, 401, 2): 
    suma += i
    contador += 1

# Calcular el promedio
promedio = suma / contador if contador > 0 else 0

# Imprimir el resultado
st.write(f"La suma de los números pares entre 20 y 400 es: {suma}")
st.write(f"El promedio de los números pares entre 20 y 400 es: {promedio}")

st.write("********************************************************************************************")




#Ejercicio-08:
#De una lista de 10 números calcular la media y determinar cuántos son mayores que 10,cuantos
#son iguales y cuántos son menores.

st.subheader("Ejercicio 8: De 10 numeros calcular la media y determinar mayores, iguales o menores a 10")


numeros = []
for i in range(10):
    num = st.number_input(f"Ingrese el número {i + 1}: ", min_value=1)
    numeros.append(num)

# Calcular la media
media = sum(numeros) / len(numeros)

# Contar cuántos son mayores, iguales y menores que 10
mayores = sum(1 for num in numeros if num > 10)
iguales = sum(1 for num in numeros if num == 10)
menores = sum(1 for num in numeros if num < 10)

# Imprimir los resultados
st.write(f"La media de los números es: {media}")
st.write(f"Números mayores que 10: {mayores}")
st.write(f"Números iguales a 10: {iguales}")
st.write(f"Números menores que 10: {menores}")

st.write("********************************************************************************************")



#Ejercicio-09
#Calcular la media de N números dados e imprimir su resultado.

st.subheader("Ejercicio 9: Calcular la media de N números dados e imprimir su resultado")

N = st.number_input("Ingrese la cantidad de números a promediar: ", min_value=1)

suma = 0

# Solicitar al usuario que ingrese los números y calcular la suma
for i in range(N):
    num = st.number_input(f"Ingrese el número {i + 1}: ")
    suma += num

# Calcular la media
media = suma / N if N > 0 else 0

# Imprimir el resultado
st.write(f"La media de los {N} números es: {media}")


st.write("********************************************************************************************")


#Ejercicio-10
#Dado N notas de un estudiante calcular: 
#Cuantas notas tiene desaprobados. Cuantos aprobados. El promedio de todas las notas.

st.subheader("Ejercicio 10: Calcular notas de un estudiante")

Numx = st.number_input("Ingrese la cantidad de notas: ", min_value=1, step=1)

aprobados = 0
desaprobados = 0
sumax = 0
# Solicitar las notas y calcular
for i in range(Numx):
    nota = st.number_input(f"Ingrese la nota {i + 1}: ")
    sumax += nota
    
    if nota >= 11:  # Asumiendo que la nota mínima para aprobar es 6
        aprobados += 1
    else:
        desaprobados += 1
# Calcular el promedio
promedio = sumax / Numx if Numx > 0 else 0

# Imprimir los resultados
st.write(f"Número de notas aprobadas: {aprobados}")
st.write(f"Número de notas desaprobadas: {desaprobados}")
st.write(f"Promedio de las notas: {promedio:.2f}")
st.write("********************************************************************************************")


#Ejercicio-11
#Crea un programa que pida al usuario una contraseña, de forma repetitiva mientras que no 
#introduzca “asdasd”. Cuando finalmente escriba la contraseña correcta, se le dirá “Bienvenido” y 
#terminará el programa.
st.subheader("Ejercicio 11: Login")
def verificar_contrasena():
    st.title("Verificación de contraseña")
    # Contraseña correcta
    contrasena_correcta = "asdasd"
    # Inicializar variable de sesión para almacenar la entrada del usuario
    if "contrasena_ingresada" not in st.session_state:
        st.session_state.contrasena_ingresada = ""
    # Input de la contraseña
    contrasena_ingresada = st.text_input("Introduce la contraseña:", type="password")
    # Botón para verificar la contraseña
    if st.button("Verificar"):
        if contrasena_ingresada == contrasena_correcta:
            st.session_state.contrasena_ingresada = contrasena_ingresada
            st.success("Bienvenido")
        else:
            st.error("Contraseña incorrecta, intenta de nuevo")
# Llamada a la función principal
if __name__ == "__main__":
    verificar_contrasena()
st.write("********************************************************************************************")



#Ejercicio-12
#Crear un programa, que permita hallar el área y perímetro de una circunferencia.

import math

st.subheader("Ejercicio 12: Hallar el área y perímetro de una circunferencia")
def calcular_area(radio):
    return math.pi * (radio**2)

def calcular_perimetro(radio):
    return 2 * math.pi * radio

def main():
    st.title("Calculo del área y perímetro de una circunferencia")
    radio = st.number_input("Ingrese el radio de la circunferencia", min_value=0.0, step=0.1)
    if radio > 0:
        area = calcular_area(radio)
        perimetro = calcular_perimetro(radio)
        st.write(f"Area: {area:.2f}")
        st.write(f"Perimetro: {perimetro:.2f}")
    else:
        st.write("Por favor, ingrese un radio mayor a CERO")
if __name__ == "__main__":
    main()
st.write("********************************************************************************************")





#Ejercicio-13
#Crear una calculadora de las 4 operaciones basicas 
st.subheader("Ejercicio 13: Calculadora con las 4 operaciones básicas")

def suma(a, b):
    return a + b
def resta(a, b):
    return a - b
def multiplicacion(a,b):
    return a * b
def division(a,b):
    if b != 0:
        return a/b
    else:
        return "Error: División por cero"

def main():
    st.title("Calculadora Básica")
    #Entrada de datos
    numero1 = st.number_input("Ingrese el primer número:", format="%f")
    numero2 = st.number_input("Ingrese el segundo número:", format="%f")
    #Selección de operación
    operacion = st.selectbox("Seleccione la operación", ("Suma", "Resta", "Multiplicación", "División"))
    #Realizar la operación seleccionada
    if operacion == "Suma":
        resultado = suma(numero1, numero2)
    elif operacion == "Resta":
        resultado = resta(numero1, numero2)
    elif operacion == "Multiplicación":
        resultado = multiplicacion(numero1, numero2)
    elif operacion == "División":
        resultado = division(numero1, numero2)
    #monstrar el resultado
    st.write(f"Resultado: {resultado}")

if __name__ == "__main__":
    main()

st.write("********************************************************************************************")
