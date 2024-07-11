import altair as alt
import streamlit as st
import pandas as pd
import folium
from folium.plugins import FastMarkerCluster
from streamlit_folium import st_folium


def number_to_text(x):
    return "Si" if x == 1 else "No"


@st.cache_data
def load_data(data_path):
    df = pd.read_csv(data_path)
    df.es_superhost = df.es_superhost.map(number_to_text)
    df.servicio_aire_acondicionado = df.servicio_aire_acondicionado.map(number_to_text)
    return df


def add_title_and_description():
    print("Cargando título")
    st.title("Airbnb")
    st.markdown("Este es un análisis de los datos de Airbnb en la Ciudad de México")


def show_airbnb_dataframe(df):
    print("Cargando dataframe")
    camas=st.slider("cantidad mínima de camas", #min #max #value #step
               1,16,16,2)
    st.write("Camas: ",camas)
    st.write(df[df.capacidad>=camas])
    #st.dataframe(df)


def country_filter(df):
    pass


def show_airbnb_in_map(df, is_all_data):
    pass


def plot_days_of_week(df, column):
    pass


def plot_airbnb_by_superhost(df, column):
    pass


def interactive_view(df):
    pass


if __name__ == "__main__":
    df = load_data("Airbnb_Locations.csv")
    add_title_and_description()
    show_airbnb_dataframe(df)
    
    #Improvisar
    st.header("Gráfico de pastel")
    pie = alt.Chart(df).mark_arc().encode(
        theta="count()", color="es_superhost:N")
    st.altair_chart(pie)

    #1. Hacer un gráfico
    #2. Subir el código a un repositorio de github
    #3. Compartir el link del repositorio
    #4. Compartir el link de la app
    

    # Descomentar a medida que avancemos

    # filtered_df = country_filter(df)
    # show_airbnb_in_map(filtered_df, filtered_df.shape == df.shape)
    # column_1, column_2 = st.columns(2)
    # plot_days_of_week(filtered_df, column_1)
    # plot_airbnb_by_superhost(filtered_df, column_2)
    # interactive_view(filtered_df)
