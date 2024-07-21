
import streamlit as st 
import pandas as pd 
import time 
  
df = pd.read_csv("iris.csv") 
  
col = st.sidebar.multiselect("Select any column", 
                             df.columns) 
  
prg = st.progress(0) 
  
for i in range(100): 
    time.sleep(0.1) 
    prg.progress(i+1) 
st.dataframe(df[col])
