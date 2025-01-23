import streamlit as st
import pandas as pd
import seaborn as sns

uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
    
    # Read et Edition
    df  = pd.read_csv(uploaded_file, delimiter=',')
    
    # Multichoice select
    selected_columns = st.multiselect("Sélectionner les colonnes a télécharger", df.columns)
    edited_df = st.data_editor(df[selected_columns])
    
    with st.form(key='my_form'):
    
        col1, col2 = st.columns(2)
        
        with col1:
            # SelectBox
            columnX = st.selectbox("Sélectionner X", edited_df.columns)
            
            numerics = ['int16', 'int32', 'int64', 'float16', 'float32', 'float64']
            columnY = st.selectbox("Sélectionner Y (Valeur numerique)", edited_df.select_dtypes(include=numerics).columns)
            # Slider
            #range_min, range_max = st.slider('Sélectionnez une tranche d\'âge', df.Age.min(), df.Age.max(), (30, 80))
        
            #data = df[(df.Profession == profession) & (df.Age >= range_min) & (df.Age <= range_max)].Age
            if st.form_submit_button(label='Valider'):
                with col2:
                    st.dataframe(edited_df[[columnX, columnY]].groupby(by=[columnX]).mean())
                    plot = sns.barplot(edited_df[[columnX, columnY]].groupby(by=[columnX]).mean(), x=columnX, y=columnY)
                    st.pyplot(plot.figure)
    
    
    
    
    #Download
    st.download_button(
    label="Download data as CSV",
    data=edited_df.to_csv(),
    file_name="large_df.csv",
    mime="text/csv",
)