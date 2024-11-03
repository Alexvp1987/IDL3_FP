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

x = st.number_input("Ingrese el valor de x: ", min_value=1))

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
