import streamlit as st
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns

st.title("HR Performance Dashboard")

data = {
   "performance_rating":[2,3,4,3,4,2,3,3,4,2],
  "training_hours":[10,15,8,20,12,16,9,18,14,10]
}

df = pd.DataFrame(data)

st.subheader("Performance Rating Distributuion")

fig, ax= plt.subplots()
sns.countplot(x="performance_rating", data=df,ax=ax)

st.pyplot(fig)
  
