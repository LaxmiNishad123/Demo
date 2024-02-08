import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


st.title('IRIS FLOWER DASHBOARD')
st.sidebar.subheader('Description')
st.divider()
col1,col2=st.columns(2) 
with col1:
    st.header('Pie Chart of Species')
   
with col2:
    st.header('Bar Chart of Species')
   

