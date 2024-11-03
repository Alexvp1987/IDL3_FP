#Ejercicio-01: 
#Se requiere el código en python para imprimir en pantalla 10 veces el texto “HolaMundo”.

import streamlit as st

st.title("Ejercicios para el IDL3")
st.subheader("Ejercicio 1: Imprimir en pantalla 10 veces el texto HolaMundo")

for i in range(10):
    st.write("HolaMundo")

st.write("********************************************************************************************")

