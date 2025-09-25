# Importar streamlit
import streamlit as st

# Configurar la pagina
st.set_page_config(
    page_title="Bestiario MH",
    page_icon=":yellow_heart:", # Usar el comando python -m rich.emoji para ver lista de emojis
    layout="centered",
)

# Configuración de Logo

# Barra de navegacion, crear las multipaginas
pg = st.navigation(["intro_y_magnamalo.py", "fatalis.py", "valstrax.py", "malzeno.py", "quien.py"])


pg.run()
