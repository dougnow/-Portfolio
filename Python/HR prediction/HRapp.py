#!/usr/bin/env python
# coding: utf-8

# In[1]:


import streamlit as st
import joblib
import numpy as np

# Cargar el modelo entrenado
modelo = joblib.load('modelo_SVC_entrenado.pkl')

st.title("Predicción de Resignación de Empleados")

# Inputs del usuario
education = st.selectbox("Education", ["Bachelors", "Masters", "PHD"])
joining_year = st.number_input("Joining Year", min_value=2000, max_value=2025, step=1)
city = st.selectbox("City", ["Bangalore", "Pune", "New Delhi"])
payment_tier = st.selectbox("Payment Tier", [1, 2, 3])
age = st.number_input("Age", min_value=18, max_value=60)
gender = st.selectbox("Gender", ["Male", "Female"])
ever_benched = st.selectbox("Ever Benched", ["No", "Yes"])
experience = st.number_input("Experience in Current Domain", min_value=0, max_value=10)

# Convertir inputs categóricos a valores numéricos
education_mapping = {"Bachelors": 0, "Masters": 1, "PHD": 2}
city_mapping = {"Bangalore": 0, "Pune": 1, "New Delhi": 2}
gender_mapping = {"Male": 0, "Female": 1}
ever_benched_mapping = {"No": 0, "Yes": 1}

input_data = np.array([
    education_mapping[education],
    joining_year,
    city_mapping[city],
    payment_tier,
    age,
    gender_mapping[gender],
    ever_benched_mapping[ever_benched],
    experience
]).reshape(1, -1)

# Predicción
if st.button("Predecir"):
    resultado = modelo.predict(input_data)
    if resultado[0] == 1:
        st.write("El empleado tiene alta probabilidad de renunciar.")
    else:
        st.write("El empleado tiene baja probabilidad de renunciar.")


# In[ ]:




