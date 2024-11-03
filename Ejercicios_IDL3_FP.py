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
    print(i)

st.write("********************************************************************************************")


