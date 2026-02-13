import streamlit as st
import pandas as pd

st.title("Interaction with DataFrames")
file = st.file_uploader("Upload a CSV file", type=["csv"])
if file:
    df = pd.read_csv(file)
    st.write("DataFrame:")
    st.dataframe(df)
    
if file:
    st.write("Summary Statistics:")
    st.write(df.describe())
    
if file:
    selected_city = df['City'].unique()
    filtered_df = df[df["City"] == selected_city]
    st.dataframe(filtered_df)