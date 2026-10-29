from PIL import Image
import streamlit as st

st.title("Portafolio Interfaces Multimodales")

with st.sidebar:
    st.subheader("Maria José Melo Ceron")
    parrafo = "portafolio 1"
    st.write(parrafo)

url_ia = "https://sites.google.com/view/aplicacionesdeia/inicio"
st.subheader(
    f"en cada enlace estan las paginas modificadas a lo largo del semestre hasta ahora: [Enlace]({url_ia})"
)
col1, col2, col3, col4, col5, col6 = st.columns(6)

with col1:
    with st.container(border=True):
        st.subheader("detección de objetos en imagenes")
        image = Image.open("primerafoto.jpg")
        st.image(image, width=190)
        st.write("toma una foto y la app reconoce objetos")
        url = "https://yolov5profe-pvibkrfl3nvpzax9yostns.streamlit.app/"
        st.write(f"enlace: [Enlace]({url})")

    with st.container(border=True):
        st.subheader("primera prueba")
        image = Image.open("segundafoto.png")
        st.image(image, width=200)
        st.write("primera prueba en streamlit")
        url = "https://wordcloudprofe-wtjxd8rnzefwmccgipsaz5.streamlit.app/"
        st.write(f"enlace: [Enlace]({url})")

    with st.container(border=True):
        st.subheader("Buscador de Cuentos e Historias")
        image = Image.open("tercerafoto.jpg")
        st.image(image, width=200)
        st.write(
            "Esta herramienta analiza un conjunto de cuentos o frases breves y encuentra la historia que mejor responde a tu pregunta."
        )
        url = "https://tfidfprofe-gnvdiqmhpnsrj5sdhw5ifd.streamlit.app/"
        st.write(f"enlace: [Enlace]({url})")

with col2:
    with st.container(border=True):
        st.subheader("emociones")
        image = Image.open("cuartafoto.jpg")
        st.image(image, width=200)
        st.write(
            "interfaz para que niños pequeños vayan aprendiendo como identificar sus emociones y que hacer en cada caso."
        )
        url = "https://sentimentaprofe-vsuq47r9wypxomxchduzy3.streamlit.app/"
        st.write(f"enlace: [Enlace]({url})")

    with st.container(border=True):
        st.subheader("asistente de audio")
        image = Image.open("quintafoto.jpg")
        st.image(image, width=190)
        st.write("Escribe el texto y reproducelo como audio")
        url = "https://imm1prf-mgsgcrtdgkqgrqggmzmi3k.streamlit.app/"
        st.write(f"enlace: [Enlace]({url})")

    with st.container(border=True):
        st.subheader("segunda prueba")
        image = Image.open("sextafoto.jpg")
        st.image(image, width=200)
        st.write("segunda prueba subiendo una app a srteamlit")
        url = "https://clase6vozaudio-pgcremuqmkzschba63zxqe.streamlit.app/"
        st.write(f"enlace: [Enlace]({url})")

with col3:
    with st.container(border=True):
        st.subheader("Escáner Inteligente de Texto (OCR)")
        image = Image.open("septimafoto.jpg")
        st.image(image, width=190)
        st.write(
            "Captura una imagen o documento para extraer su contenido en texto automáticamente."
        )
        url = "https://imagenrecogmj-bqibrtptajf5o7xkm6spfm.streamlit.app/"
        st.write(f"enlace: [Enlace]({url})")

    with st.container(border=True):
        st.subheader("Lector OCR & Traductor de Voz")
        image = Image.open("octavafoto.jpg")
        st.image(image, width=200)
        st.write(
            "Extrae texto de una imagen (cámara o archivo), tradúcelo y escúchalo en audio."
        )
        url = "https://ocr-moremj-mz2heyh3kieiu5bk527zbt.streamlit.app/"
        st.write(f"enlace: [Enlace]({url})")

    with st.container(border=True):
        st.subheader("Sistema Ciberfísico")
        image = Image.open("fotoultima.jpg")
        st.image(image, width=200)
        st.write(
            "En la siguiente enlace veremos la capacidad de interacción con el mundo físico."
        )
        url = "https://vision2-gpt4o.streamlit.app/"
        st.write(f"Vision: [Enlace]({url})")

with col4:
    with st.container(border=True):
        st.subheader("Chat Pdf")
        image = Image.open("uno.jpg")
        st.image(image, width=200)
        st.write(
            "Es una plataforma interactiva que permite subir archivos PDF para analizarlos, chatear con su contenido y extraer información o resúmenes mediante inteligencia artificial."
        )
        url = "https://chatpdfport2-xkgdb9qpj6vg87bfan3pa9.streamlit.app/"
        st.write(f"Vision: [Enlace]({url})")

    with st.container(border=True):
        st.subheader("Vision app")
        image = Image.open("dos.jpg")
        st.image(image, width=200)
        st.write(
            "Es una herramienta web interactiva para cargar imágenes, proporcionar contexto y analizarlas automáticamente utilizando inteligencia artificial."
        )
        url = "https://visionappport2-xhkwdzxgm7vxvluqsxv8ed.streamlit.app/"
        st.write(f"Vision: [Enlace]({url})")

    with st.container(border=True):
        st.subheader("Tablero")
        image = Image.open("tres.jpg")
        st.image(image, width=200)
        st.write(
            "Es una plataforma interactiva que permite visualizar y consultar tableros de datos o información estructurada para el análisis rápido de métricas."
        )
        url = "https://tableroclase12-6fqvhz8freadge5geehewh.streamlit.app/"
        st.write(f"Vision: [Enlace]({url})")

with col5:
    with st.container(border=True):
        st.subheader("Clasificador de Dígitos MNIST con Inteligencia Artificial")
        image = Image.open("cuatro.jpg")
        st.image(image, width=200)
        st.write(
            "Es una herramienta web interactiva diseñada para reconocer y clasificar dígitos escritos a mano mediante modelos de aprendizaje automático."
        )
        url = "https://mnistpredprofe12-xs4kjswwbs3wgvqyxsboqh.streamlit.app/"
        st.write(f"Vision: [Enlace]({url})")

    with st.container(border=True):
        st.subheader("Reconocimiento de Dibujos con Inteligencia Artificial")
        image = Image.open("cinco.jpg")
        st.image(image, width=200)
        st.write(
            "Es una herramienta web interactiva que permite dibujar trazos a mano alzada para que un modelo de aprendizaje automático los reconozca y clasifique en tiempo real."
        )
        url = "https://drawrecogprofe12-bm6fzftarnag8o7drbdlzu.streamlit.app/"
        st.write(f"Vision: [Enlace]({url})")

    with st.container(border=True):
        st.subheader("Transmisor de Comandos por MQTT")
        image = Image.open("seis.jpg")
        st.image(image, width=200)
        st.write(
            "Es una herramienta web interactiva diseñada para enviar mensajes y comandos de control a través de un protocolo de comunicación MQTT en tiempo real."
        )
        url = "https://sendcmqttprofe13-faqbvmbbfgzf5kpqd7mby5.streamlit.app/"
        st.write(f"Vision: [Enlace]({url})")

with col6:
    with st.container(border=True):
        st.subheader("Panel de Control por Voz Multimodal")
        image = Image.open("siete.jpg")
        st.image(image, width=200)
        st.write(
            "Es una herramienta web interactiva que permite capturar comandos de voz mediante el navegador para transmitirlos en tiempo real a través de un protocolo de comunicación MQTT."
        )
        url = "https://ctrlvoiceport2-pnkdgmn7ce36pawq86hc4k.streamlit.app/"
        st.write(f"Vision: [Enlace]({url})")


