import streamlit as st
import replicate
from PIL import Image
import requests
from io import BytesIO
from transformers import pipeline
from streamlit_image_comparison import image_comparison

# --- CONFIGURACIÓN DE LA PÁGINA ---
st.set_page_config(
    page_title="Restaurador de Recuerdos IA",
    page_icon="✨",
    layout="wide"
)

# --- TÍTULO Y DESCRIPCIÓN (USER PERSONA: LAURA) ---
st.title("✨ Restaurador de Recuerdos IA")
st.markdown("""
**¡Bienvenida/o!** Esta herramienta utiliza Inteligencia Artificial Generativa para recuperar detalles en fotos antiguas o de baja calidad.

1.  **Sube tu foto** borrosa o antigua.
2.  La IA **restaurará los detalles** (especialmente rostros).
3.  Analizaremos la **calidad técnica** del resultado.
""")

# --- SIDEBAR: CONFIGURACIÓN ---
with st.sidebar:
    st.header("⚙️ Configuración")
    st.info("Para usar el modelo de restauración potente (GFPGAN), necesitamos un token de Replicate.")
    
    # Input para la API Key (Seguridad: no la hardcodeamos)
    replicate_api_token = st.text_input("Ingresá tu Replicate API Token:", type="password")
    st.markdown("[Obtener token gratis aquí](https://replicate.com/account/api-tokens)")
    
    st.divider()
    st.subheader("Opciones de Restauración")
    version_modelo = st.selectbox(
        "Modelo de IA",
        ["GFPGAN (Especialista en Rostros)", "Real-ESRGAN (General)"]
    )
    scale = st.slider("Escala de Aumento (Upscaling)", 2, 4, 2)

# --- FUNCIONES ---

@st.cache_resource
def cargar_modelo_analisis():
    """Carga el modelo CLIP de Hugging Face para análisis local."""
    # Usamos CLIP para clasificación Zero-Shot (sin entrenamiento)
    return pipeline("zero-shot-image-classification", model="openai/clip-vit-base-patch32")

def analizar_imagen(image, pipe):
    """Analiza la calidad de la imagen usando CLIP."""
    # Definimos categorías descriptivas para que la IA elija
    labels = ["imagen nítida de alta definición", "imagen borrosa o pixelada", "foto antigua dañada", "fotografía profesional"]
    results = pipe(image, candidate_labels=labels)
    return results

def procesar_imagen(uploaded_file, api_token, modelo):
    """Envía la imagen a Replicate para restauración."""
    if not api_token:
        st.error("⚠️ Por favor ingresá tu API Token de Replicate en la barra lateral.")
        return None

    # Configurar cliente
    client = replicate.Client(api_token=api_token)
    
    # Seleccionar modelo
    model_id = ""
    input_params = {}

    if modelo == "GFPGAN (Especialista en Rostros)":
        # Modelo GFPGAN en Replicate
        model_id = "tencentarc/gfpgan:9283608cc6b7be6b65a8e44983db012355fde4132009bf99d976b2f0896856a3"
        input_params = {"img": uploaded_file, "scale": scale}
    else:
        # Modelo Real-ESRGAN
        model_id = "nightmareai/real-esrgan:42fed1c4974146d4d2414e2be2c5277c7fcf05fcc3a73abf41610695738c1d7b"
        input_params = {"image": uploaded_file, "scale": scale, "face_enhance": True}

    try:
        output = client.run(model_id, input=input_params)
        return output # Devuelve URL de la imagen procesada
    except Exception as e:
        st.error(f"Error al procesar: {e}")
        return None

# --- UI PRINCIPAL ---

uploaded_file = st.file_uploader("Arrastrá tu imagen aquí (JPG/PNG)", type=['jpg', 'png', 'jpeg'])

if uploaded_file:
    # 1. Mostrar Imagen Original
    image_original = Image.open(uploaded_file).convert("RGB")
    
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Original")
        st.image(image_original, use_column_width=True)

    # Botón de acción
    if st.button("🚀 Restaurar Imagen con IA", type="primary"):
        if not replicate_api_token:
            st.warning("Necesitás ingresar el token en la barra lateral primero.")
        else:
            with st.spinner("⏳ La IA está reconstruyendo píxeles... (Esto toma unos segundos)"):
                
                # A. PROCESAMIENTO (DIFUSIÓN/GAN)
                output_url = procesar_imagen(uploaded_file, replicate_api_token, version_modelo)
                
                if output_url:
                    # Descargar resultado
                    response = requests.get(output_url)
                    image_restored = Image.open(BytesIO(response.content)).convert("RGB")

                    # B. ANÁLISIS VISUAL (HUGGING FACE TRANSFOMERS)
                    with st.status("🔍 Analizando calidad visual con CLIP..."):
                        analizador = cargar_modelo_analisis()
                        analisis_orig = analizar_imagen(image_original, analizador)
                        analisis_rest = analizar_imagen(image_restored, analizador)
                    
                    # C. MOSTRAR RESULTADOS
                    with col2:
                        st.subheader("Restaurada")
                        st.image(image_restored, use_column_width=True)
                    
                    st.divider()
                    
                    # Componente de comparación "Slider" (Requisito visual)
                    st.subheader("🆚 Comparación Interactiva")
                    st.write("Desliza hacia los lados para ver la magia:")
                    image_comparison(
                        img1=image_original,
                        img2=image_restored,
                        label1="Original",
                        label2="Restaurada",
                    )

                    # Sección de Análisis Inteligente
                    st.divider()
                    st.subheader("🧠 Análisis de Visión por Computadora (CLIP)")
                    
                    ac1, ac2 = st.columns(2)
                    
                    with ac1:
                        top_label = analisis_orig[0]['label']
                        score = analisis_orig[0]['score']
                        st.info(f"La IA ve la **Original** como: \n\n **'{top_label}'** ({score:.1%} confianza)")
                        
                    with ac2:
                        top_label_r = analisis_rest[0]['label']
                        score_r = analisis_rest[0]['score']
                        # Lógica simple de feedback
                        if "nítida" in top_label_r or "profesional" in top_label_r:
                            st.success(f"La IA ve la **Restaurada** como: \n\n **'{top_label_r}'** ({score_r:.1%} confianza)")
                        else:
                            st.warning(f"La IA clasifica la restaurada como: '{top_label_r}'")

    else:
        st.info("👆 Carga una imagen y presiona el botón para comenzar.")

# --- FOOTER ---
st.divider()
st.markdown("Desarrollado para la materia Procesamiento Digital de Imágenes - IFTS 24")