
import streamlit as st
import pandas as pd

uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
    
    df  = pd.read_csv(uploaded_file, delimiter=';')
    edited_df = st.data_editor(df)
    
    st.download_button(
    label="Download data as CSV",
    data=edited_df.to_csv(),
    file_name="large_df.csv",
    mime="text/csv",
)