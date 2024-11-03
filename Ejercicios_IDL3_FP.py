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

#N = st.number_input("Ingrese la cantidad de números a promediar: ", min_value=1)
N = st.float("Ingrese la cantidad de números a promediar: ", min_value=1)

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
