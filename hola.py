import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


st.title('Aplicación de gráficas')


st.header('Demo App')


st.write('Demo de sitio con gráficas')


titanic_data = pd.read_csv('titanic(1).csv')
st.dataframe(titanic_data)

fig, ax = plt.subplots()
ax.hist(titanic_data['Fare'])
st.header('Histograma del Titanic')
st.pyplot(fig)

fig2, ax2 = plt.subplots()
y_pos = titanic_data['Pclass']
x_pos = titanic_data['Fare']
ax2.barh(y_pos, x_pos)
ax2.set_ylabel('Class')
ax2.set_xlabel('Fare')
ax2.set_title('¿Cuanto pagaron las clases del Titanic?')
st.header('Gráfica de barras del Titanic')
st.pyplot(fig2)

st.header('Diagrama de dispersión: Edad vs Tarifa')
fig3, ax3 = plt.subplots()
ax3.scatter(titanic_data['Age'], titanic_data['Fare'])
ax3.set_xlabel('Age')
ax3.set_ylabel('Fare')
ax3.set_title('Relación entre la edad y la tarifa')
st.pyplot(fig3)

st.header('Gráfico de caja: Distribución de tarifas por clase')
fig4, ax4 = plt.subplots()
titanic_data.boxplot(column='Fare', by='Pclass', ax=ax4)
plt.title('Distribución de tarifas por clase')
plt.suptitle('')  
st.pyplot(fig4)

st.header('Gráfico de pastel: Proporción de pasajeros por clase')
fig5, ax5 = plt.subplots()
titanic_data['Pclass'].value_counts().plot(kind='pie', ax=ax5, autopct='%1.1f%%')
ax5.set_ylabel('')
ax5.set_title('Pasajeros por clase')
st.pyplot(fig5)

st.header('Gráfico de líneas: Variación de tarifas')
fig6, ax6 = plt.subplots()
titanic_data['Fare'].plot(ax=ax6)
ax6.set_ylabel('Fare')
ax6.set_title('Variación de tarifas en el dataset')
st.pyplot(fig6)

st.header('Gráfico de densidad: Distribución de edades')
fig7, ax7 = plt.subplots()
titanic_data['Age'].plot(kind='density', ax=ax7)
ax7.set_xlabel('Age')
ax7.set_title('Distribución de edades')
st.pyplot(fig7)

st.markdown('-----')



