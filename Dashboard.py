import streamlit as st
import pandas as pd
import seaborn as sns

path = 'https://raw.githubusercontent.com/Quera-fr/Python-Programming/refs/heads/main/data.csv'
df = pd.read_csv(path)

st.set_page_config(
    page_title="My Dashboard",
    page_icon="",
    layout="wide"
)

st.title('My Dashboard')
st.subheader('Présentation de données')

st.write('Présentation de données avec Streamlit')

if st.checkbox('Afficher le formulaire'):
    #name = st.text_input('Entrez votre nom')
    #st.write(f'Bonjour {name}')
    st.write(df)
    
#st.sidebar.image('https://media.licdn.com/dms/image/v2/D4D10AQHVgpzPmHzAVA/image-shrink_800/image-shrink_800/0/1719911703867?e=2147483647&v=beta&t=JRcTlqNJu_CbhKlGEHkbSfmWPuIu5qfVzg6nAPjhlr0')
#st.sidebar.video('https://www.youtube.com/watch?v=dQw4w9WgXcQ')

#Formulaire
with st.form(key='my_form'):
    
    col1, col2 = st.columns(2)
    
    with col1:
        # SelectBox
        profession = st.selectbox("Sélectionner une profession", df.Profession.unique())
        # Slider
        range_min, range_max = st.slider('Sélectionnez une tranche d\'âge', df.Age.min(), df.Age.max(), (30, 80))
    
        data_age = df[(df.Profession == profession) & (df.Age >= range_min) & (df.Age <= range_max)].Age
        if st.form_submit_button(label='Valider'):
            with col2:
                plot = sns.histplot(data_age, bins= range_max - range_min)
                st.pyplot(plot.figure)