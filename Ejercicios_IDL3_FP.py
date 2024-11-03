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
