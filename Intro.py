import streamlit as st
from PIL import Image
st.title("Portafolio Interfaces Multimodales")

with st.sidebar:
  st.subheader("Maria José Melo Ceron")
  parrafo = (
    "portafolio 1"
  )
  st.write(parrafo)

url_ia="https://sites.google.com/view/aplicacionesdeia/inicio"
st.subheader("en cada enlace estan las paginas modificadas a lo largo del semestre hasta ahora: [Enlace]({url_ia})")
col1, col2, col3 = st.columns(3)

with col1:
 
 st.subheader("detección de objetos en imagenes")
 image = Image.open('primerafoto.jpg')
 st.image(image, width=190)
 st.write("toma una foto y la app reconoce objetos") 
 url = "https://yolov5profe-pvibkrfl3nvpzax9yostns.streamlit.app/"
 st.write(f"enlace: [Enlace]({url})")

 st.subheader("primera prueba")
 image = Image.open('segundafoto.png')
 st.image(image, width=200)
 st.write("primera prueba en streamlit") 
 url = "https://wordcloudprofe-wtjxd8rnzefwmccgipsaz5.streamlit.app/"
 st.write(f"enlace: [Enlace]({url})")

 st.subheader("Buscador de Cuentos e Historias")
 image = Image.open('tercerafoto.jpg')
 st.image(image, width=200)
 st.write("Esta herramienta analiza un conjunto de cuentos o frases breves y encuentra la historia que mejor responde a tu pregunta.") 
 url = "https://tfidfprofe-gnvdiqmhpnsrj5sdhw5ifd.streamlit.app/"
 st.write(f"enlace: [Enlace]({url})")

with col2: 
 st.subheader("emociones")
 image = Image.open('cuartafoto.jpg')
 st.image(image, width=200)
 st.write("interfaz para que niños pequeños vayan aprendiendo como identificar sus emociones y que hacer en cada caso.") 
 url = "https://sentimentaprofe-vsuq47r9wypxomxchduzy3.streamlit.app/"
 st.write(f"enlace: [Enlace]({url})")

 st.subheader("asistente de audio")
 image = Image.open('quintafoto.jpg')
 st.image(image, width=190)
 st.write("Escribe el texto y reproducelo como audio") 
 url = "https://imm1prf-mgsgcrtdgkqgrqggmzmi3k.streamlit.app/"
 st.write(f"enlace: [Enlace]({url})")

 st.subheader("Trasnscriptor Audio y Video")
 image = Image.open('OIG3.jpg')
 st.image(image, width=200)
 st.write("En la siguiente enlace veremos como realizamos transcripciones de audio/video.") 
 url = "https://transcript-whisper.streamlit.app/"
 st.write(f"Transcriptor: [Enlace]({url})")


with col3: 
 st.subheader("Generación en Contexto")
 image = Image.open('Chat_pdf.png')
 st.image(image, width=190)
 st.write("En la siguiente veremos una aplicación que usa RAG a partir de un documento (PDF).") 
 url = "https://chatpdf-cc.streamlit.app/"
 st.write(f"RAG: [Enlace]({url})")

 st.subheader("Análisis de Imagen")
 image = Image.open('OIG4.jpg')
 st.image(image, width=200)
 st.write("En la siguiente enlace veremos la capacidad de análisis en Imágenes.") 
 url = "https://vision2-gpt4o.streamlit.app/"
 st.write(f"Vision: [Enlace]({url})")
 
 st.subheader("Sistema Ciberfísico")
 image = Image.open('OIG6.jpg')
 st.image(image, width=200)
 st.write("En la siguiente enlace veremos la capacidad de interacción con el mundo físico.") 
 url = "https://vision2-gpt4o.streamlit.app/"
 st.write(f"Vision: [Enlace]({url})")


