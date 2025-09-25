# Importar streamlit
import streamlit as st
#linea de titulo
st.header("Malzeno", divider=True)
#linea de imagen
st.image("malzenoM.jpg", caption="Malzeno")
#linea de audio
st.audio("malzenoR.mp3")
#linea de escritura
st.write("**Informacion del Malzeno** | Créditos: https://monsterhunter.fandom.com/es/wiki/Malzeno")

st.markdown(
"""
1. Apariencia
-Su cabeza está adornada por dos cuernos dorados, además de una especie de dos collarines. En su cuello cuelgan los Qurio. Sus alas son grises con cierto tono negruzco, adornadas con dos garras doradas. Por la parte interna son de color carmesí. Sus patas son esbeltas, acabadas en garras del mismo tono dorado que sus cuernos, además que su cola acaba en tres pinchos que usa para rematar a sus presas.

2. Ecología
-Es un dragón anciano solitario. Tiene una relación simbólica con los Qurio: estos debilitan a la presa del Malzeno y este aprovecha la debilidad de su presa para rematarla con su cola, acabada en tres pinchos letales. Habita principalmente en el Bastión, lugar que atacó y transformó en su hábitat, además de proclamarse el amo y señor del territorio.

3. Combate
-Es un contrincante rápido. Sus ataques infligen Plaga Sangrienta, que mermará tu salud poco a poco. Para librarte de la Plaga Sangrienta, ataca a Malzeno. Recuperarás un poco de vida con cada ataque hasta estar curado. Cuenta con varios ataques, como arremeter con sus alas o teletransportarse tras cubrirse con estas. Puede entrar en un estado cargado en el que es más agresivo y aprovechará los ataques a base de Qurio. Ten cuidado con su cola, puede causar muchísimo daño con ella.

4. Notas recopilada
-Malzeno está basado en los vampiros de la mitología europea, y combina elementos góticos así como temas como aristocracia, nobleza y astucia.

-Para alimentarse Malzeno cazará Capabras o Slagtoth y mandará a los Qurio para que drenen su energía vital.

-Malzeno se considera uno de los "Tres Señores del Reino" junto a Garangolm y Lunagaron.

-La boca del Malzeno no puede cerrarse completamente sin que sus dientes superiores atraviesen su mandíbula inferior.

""")
#linea de video
st.video("https://youtu.be/oG4rj2Y-QUY?si=F7R3nOWT_Vs4XyD2")
#linea de titulo
st.header("Informacion para cazadores", divider=True)
#linea de escritura
col1, col2 = st.columns(2)
col1.write("Elemento: Draco")
col1.write("Estado: Plaga de draco, Plaga sangrienta")
col1.write("Debil contra: Draco")
col1.write("clase: Dragon Anciano")
col1.write("**Habitats: Sin habitat fijo, este es peregrino**")
col1.write("Tamaño Maximo: 2477.15cm")
col1.write("Tamaño minimo: 1873.47cm")
col1.write("Generacion: Quinta")
col1.write("Pariente o variacion: Malzeno Primordial")
col1.write("Hostilidad: Alta")
col1.write("Partes rompibles:Cabeza, lomo y patas delanteras, cola cercenable")
col1.write("Recomendacion:evadir y evitar a toda costa, solo para cazadores experimentados")
#linea de imagen
col2.image("malzenoP.jpg", caption="Malzeno Primordial")
#linea de video
col2.video("https://youtu.be/7DbTIIiLjTI?si=7gKdXPST7l32v-33")

