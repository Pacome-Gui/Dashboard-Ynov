
import streamlit as st
import pandas as pd

#Upload
uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
    
    # Read et Edition
    df  = pd.read_csv(uploaded_file, delimiter=',')
    
    # Multichoice select
    selected_columns = st.multiselect("Sélectionner les colonnes a télécharger", df.columns)
    edited_df = st.data_editor(df[selected_columns])
    
    #Download
    st.download_button(
    label="Download data as CSV",
    data=edited_df.to_csv(),
    file_name="large_df.csv",
    mime="text/csv",
)