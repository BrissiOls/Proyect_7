import pandas as pd
import plotly.express as px
import streamlit as st
        
car_data = pd.read_csv('vehicles_us.csv')  # leer los datos

st.title("Análisis de vehículos en venta")

# Casilla para histograma
show_hist = st.checkbox('Mostrar histograma de odómetro')
if show_hist:
    st.write('Histograma del odómetro de los vehículos')
    fig = px.histogram(car_data, x="odometer")
    st.plotly_chart(fig)

# Casilla para gráfico de torta
show_pie = st.checkbox('Mostrar gráfico de torta del tipo de combustible')
if show_pie:
    st.write('Distribución de tipos de combustible')
    fuel_counts = car_data['fuel'].value_counts().reset_index()
    fuel_counts.columns = ['fuel', 'count']
    pie_fig = px.pie(fuel_counts, names='fuel', values='count', title='Tipos de combustible')
    st.plotly_chart(pie_fig)

# Casilla para gráfico de dispersión
show_scatter = st.checkbox('Mostrar gráfico de dispersión Precio vs Año del Modelo')
if show_scatter:
    st.write('Relación entre precio y año del modelo')
    scatter_fig = px.scatter(car_data, x="model_year", y="price", color="fuel",
                             title="Precio vs Año del Modelo según tipo de combustible",
                             labels={"model_year": "Año del Modelo", "price": "Precio"})
    st.plotly_chart(scatter_fig)
