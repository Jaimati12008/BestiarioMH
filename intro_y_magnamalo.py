# Importar streamlit
import streamlit as st

# ---------------------  Contenido del sitio   --------------------------#
# Sección Inicial
st.title("Bestiario MH")
st.badge("El Gremio de Cazadores", color="green", icon=":material/chevron_right:")

# Sutítulo
st.header("¿Que es este sitio web?", divider=True)

st.write(
"""
Este sitio web es destinado para fans de la saga de videojuegos Monster Hunter, esta web contiene informcaion sobre los monstruos mas dificiles de la saga pasando desde el ya clasico y conocido magnamalo hasta los peores dragones ancianos. Sin nada mas que decir empezemos con el Bestiario.
"""
    )

st.header("Magnamalo", divider=True)



st.image("magnamalo.jpg", caption="Magnamalo")
st.audio("magnamaloR.mp3")
st.write(
"""
**Magnamalo** de la saga de videojuegos Monster Hunter(MH), Magnamalo proviene de las palabras Magna (gran) y Malo (malvado). En japonés Magaimagato es una combinación de las palabras ma 魔 (demonio), gai 鎧 (armadura), maga 禍 (desastre) y to 兜 (casco). También es un juego de palabras con la expresión "magamagashi", que significa ominoso.

**Magnamalo** tiene cierto parecido con un tigre. Está protegido principalmente con una coraza de color púrpura y amarillo, mientras que su vientre es rojo. La cabeza tiene un hocico corto, sostiene dos colmillos plegables debajo de las mejillas y luce un gran par de cuernos similares a los de un ciervo, sus orejas son redondeadas. Tanto las patas delanteras como las traseras terminan en dedos de cuatro gruesas garras, y cada pata delantera está armada con una sola hoja dentada grande, que se mantiene doblada hacia atrás, paralela a la pierna. La cola de Magnamalo termina en una punta en forma de lanza compuesta por tres picos que pueden flexionarse hacia afuera para formar una forma de tridente.

**Magnamalo** es un monstruo territorial que habita en numerosos entornos, se le considera un mal augurio. Es un depredador formidable, consume numerosos monstruos para crear un gas flamígero denominado fuego infernal que utiliza como principal forma de ataque.

**Magnamalo** es un monstruo ágil y poderoso de forma similar al Zinogre. Utiliza sus patas delanteras y cola como formas principales de ataque, y también puede embestir con sus cuernos. No obstante la habilidad más temible de este monstruo es su fuego infernal. Magnamalo es capaz de lanzar orbes de fuego infernal desde su cola, y también puede soltar nubes de gas que explotan tras unos instantes con ciertos ataques. Conforme vaya atacando algunas de sus partes empezarán a expulsar fuego infernal de color rosado, lo que hará sus ataques más poderosos. Si los cazadores consiguen hacer suficiente daño a las partes en llamas, estas explotarán, dañando a Magnamalo, pero si consigue cargar al máximo su fuego infernal Magnamalo realizará un ataque devastador en el que se propulsa con su gas y explota al impactar. También es capaz de lanzar un poderoso ataque cargado desde su cola.

datos interesantes:

Para eliminar la plaga de fuego infernal se puede usar un desodorante, rodar varias veces en el suelo o realizar una evasión con el cordóptero.

**Magnamalo** está basado en una armadura samurai fantasma, y su fuego morado se basa en los fuegos fatuos.

En Sunbreak se introduce al Magnamalo Humillado, siendo Magnamalo el primer Wyvern de Colmillos en tener una variante.

"""
    )

st.video("https://youtu.be/Gyf6g2Ysb80")

st.divider()

st.header("Informacion para cazadores", divider=True)

col1, col2 = st.columns(2)
col1.write("Elemento:ninguno")
col1.write("Estado: fuego infernal")
col1.write("Debil contra: plaga de agua y rayo")
col1.write("clase:Wyvern de Colmillos")
col1.write("**Habitats: sin habitat fijo, este es peregrino**")
col1.write("Tamaño Maximo:2276.11cm")
col1.write("Tamaño minimo:1602.38cm")
col1.write("Generacion:Quinta")
col1.write("Pariente o variacion:Magnamalo Humillando/Infame")
col1.write("Hostilidad:Maxima")
col1.write("Partes rompibles:Cabeza, lomo y patas delanteras, cola cercenable")
col1.write("Recomendacion:evadir y evitar a toda costa, solo para cazadores experimentados")

col2.image("magnamalo humillado.jpg", caption="Magnamalo Humillado/Infame")
col2.video("https://youtu.be/7QHz9TUaScM")