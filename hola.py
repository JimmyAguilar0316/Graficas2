import streamlit as st
import pandas as pd 
import matplotlib.pyplot as plt 

st.title('Aplicación de gráficas')


st.header('Demo App')

st.write('Demo de sitio con gráficas')

titanic_link='titanic(1).csv'
titanic_data=pd.read_csv(titanic_link)
st.dataframe(titanic_data)

fig,ax=plt.subplots()
ax.hist(titanic_data['Fare'])
st.header('Histograma del Titanic')
st.pyplot(fig)

