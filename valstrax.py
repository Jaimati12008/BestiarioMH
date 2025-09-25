# Importar streamlit
import streamlit as st

# ---------------------  Contenido del sitio   --------------------------#
st.header("Valstrax Carmesi (La estrella de la desesperacio)", divider=True)
st.image("ValstraxC.jpg", caption="Valstrax Carmesi")

st.audio("valstraxR.mp3")

st.write("**Informacion del Valstrax Carmesi** | Créditos: https://monsterhunter.fandom.com/es/wiki/Valstrax_Carmes%C3%AD")

st.markdown(
"""
1. Apariencia
-Debido a la energía desenfrenada de draco que fluye a través de su cuerpo, Valstrax Carmesí tiene marcas rojas brillantes que se conectan desde el pecho hasta las alas, apareciendo sus costados y los brazos de las alas. Las alas tienen un diseño diferente al de las alas de un Valstrax normal, se parecen más a las rejillas de ventilación y están cubiertas de un color rojo brillante similar al de un Valstrax enfurecido normal. Al inhalar aire, las alas brillarán con un rojo brillante y comenzarán a arrojar energía de dragón. Cuando está enfurecido, la energía del dragón comienza a salir de las fosas nasales en la parte posterior de su cabeza como escape, mientras que el torso brilla de color rojo, con grandes cantidades de energía dragón saliendo de las rejillas de ventilación en el pecho y los hombros.

2. Ecología
-Es mucho más agresivo que su variante normal y se sabe que ataca indiscriminadamente cualquier cosa a la vista. Esto se debe al hecho de que su energía dragón se ha vuelto desenfrenada, alterando su comportamiento en respuesta al dolor constante causado por la energía y haciéndolo menos solitario en comparación con su contraparte normal. Debido a esto, Crimson Glow Valstrax a menudo "filtra" energía dracónica, ya sea a través de una cascada de bolas de fuego que explotan durante el vuelo, o dejando parches explosivos cada vez que ataca en su estado cargado. Como resultado, sus ataques con elemento dragón en su conjunto también se vuelven más explosivos y peligrosos.

-También tiene una tendencia a emboscar a cazadores y monstruos por igual durante la cacería bombardeándolos en picado sin previo aviso, similar a los diversos monstruos invasores como Deviljho o Bazelgeuse, siendo el indicador de emboscada la única advertencia de que Valstrax Carmesí está en el área y está listo para atacar.

3. Combate
-Se dice que Valstrax carmesí está en un nivel de amenaza equivalente a Narwa la Creadora y los monstruos Apex más fuertes del frenesí, debido a su alta agresión y nuevo poder. También es lo suficientemente valiente como para enfrentarse al Amatsu.

4. Etimologia: Valstrax proviene de Valor, Astra (estrella en latín) y Strax (inmediato en sueco). Su nombre en japonés "Valphalk" proviene de Valor y Falcon (halcón en inglés).

""")

st.video("https://youtu.be/lDbPvOrTSmA?si=mh1ubaw4WaPtTES9")

st.header("Informacion para cazadores", divider=True)

col1, col2 = st.columns(2)
col1.write("Elemento: Dragon")
col1.write("Estado: Plaga de draco")
col1.write("Debil contra: Plaga de agua, hielo, fuego y rayo")
col1.write("clase: Dragon Anciano")
col1.write("**Habitats: Sin habitat fijo, este es peregrino**")
col1.write("Tamaño Maximo: 2936.83cm")
col1.write("Tamaño minimo: 2276.11cm")
col1.write("Generacion: Quinta")
col1.write("Pariente o variacion: Valstrax")
col1.write("Hostilidad: Maxima")
col1.write("Partes rompibles:Cabeza, lomo y patas delanteras, cola cercenable")
col1.write("Recomendacion:evadir y evitar a toda costa, solo para cazadores experimentados")

col2.image("R.jpg", caption="Valstrax")

col2.video("https://youtu.be/m7wSA1-50DE?si=CUtPoEh-njewQXvi")
