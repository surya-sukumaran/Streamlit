import streamlit as st
import matplotlib .pyplot as plt 
import numpy as np
num= np.random.normal(1,5)
fig,ax=plt.subplots()
ax.hist(num,bins=10)
st.pyplot(fig)