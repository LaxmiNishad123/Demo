import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

csv_file_path = "C:\\Users\\User22\\Desktop\\Deployment_913\\Data\\Iris.csv"

df=pd.read_csv(csv_file_path)
st.title('IRIS FLOWER DASHBOARD')
st.sidebar.subheader('Description')
st.divider()
col1,col2=st.columns(2) 
with col1:
    st.header('Pie Chart of Species')
    class_data=df['class'].value_counts()
    fig, ax = plt.subplots()
    ax.pie(class_data,labels=['Setosa','versicolor','virginica'])
    st.pyplot(fig)
with col2:
    st.header('Bar Chart of Species')
    st.pyplot(df)

