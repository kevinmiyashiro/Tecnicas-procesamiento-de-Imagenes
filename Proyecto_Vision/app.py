"""
Versión estable con modelo de Teachable Machine (TensorFlow Lite)
Clasifica frutas en tres estados: maduras/frescas, verdes y podridas.
"""

import gradio as gr
import tensorflow as tf
from PIL import Image
import numpy as np
from transformers import pipeline

# ============================================
# CONFIGURACIÓN DEL MODELO PERSONALIZADO (TFLITE)
# ============================================

print("Cargando modelo TensorFlow Lite...")
interpreter = tf.lite.Interpreter(model_path="models/model_unquant.tflite")
interpreter.allocate_tensors()

input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()

with open("models/labels.txt", "r") as f:
    etiquetas_custom = [line.strip() for line in f.readlines()]

print(f"Modelo cargado correctamente con {len(etiquetas_custom)} clases.")

# ============================================
# CONFIGURACIÓN DEL MODELO CLIP (OPCIONAL)
# ============================================

modelo_clip = pipeline(
    "zero-shot-image-classification",
    model="openai/clip-vit-base-patch32"
)

CATEGORIAS_CLIP = [
    "Frutas maduras y frescas",
    "Frutas verdes sin madurar",
    "Frutas podridas"
]

# ============================================
# FUNCIONES DE PROCESAMIENTO
# ============================================

def preprocesar_imagen(imagen):
    """
    Preprocesa una imagen para el modelo de Teachable Machine.
    """
    imagen = imagen.resize((224, 224))
    img_array = np.asarray(imagen, dtype=np.float32)
    img_array = (img_array / 127.5) - 1.0
    return np.expand_dims(img_array, axis=0)


def clasificar_con_custom(imagen):
    """
    Clasifica usando el modelo de Teachable Machine (.tflite)
    """
    if imagen is None:
        return {"Error": 1.0}

    try:
        input_data = preprocesar_imagen(imagen)
        interpreter.set_tensor(input_details[0]["index"], input_data)
        interpreter.invoke()
        output_data = interpreter.get_tensor(output_details[0]["index"])[0]

        resultados = {
            etiquetas_custom[i]: float(output_data[i])
            for i in range(len(etiquetas_custom))
        }
        resultados = dict(sorted(resultados.items(), key=lambda x: x[1], reverse=True))
        return resultados
    except Exception as e:
        print(f"❌ Error en predicción personalizada: {e}")
        return {"Error": 1.0}


def clasificar_con_clip(imagen):
    """
    Clasifica usando el modelo CLIP de OpenAI (generalista).
    """
    try:
        resultados = modelo_clip(imagen, candidate_labels=CATEGORIAS_CLIP)
        return {r["label"]: float(r["score"]) for r in resultados}
    except Exception as e:
        print(f"❌ Error en CLIP: {e}")
        return {"Error": 1.0}

# ============================================
# INTERFAZ GRADIO
# ============================================

with gr.Blocks(theme=gr.themes.Soft()) as demo:
    gr.Markdown("""
    # 🍎 Clasificador de Frutas con IA

    Comparación entre:
    - Modelo **personalizado** entrenado con **Teachable Machine**
    - Modelo **CLIP** (generalista de OpenAI)
    """)

    with gr.Row():
        imagen_input = gr.Image(type="pil", label="📸 Subí o capturá una imagen", sources=["upload", "webcam"])

    with gr.Row():
        boton_custom = gr.Button("🔍 Clasificar con Modelo Personalizado", variant="primary")
        boton_clip = gr.Button("🤖 Clasificar con CLIP", variant="secondary")

    with gr.Row():
        with gr.Column():
            resultado_custom = gr.Label(label="Modelo Personalizado (Teachable)", num_top_classes=len(etiquetas_custom))
        with gr.Column():
            resultado_clip = gr.Label(label="Modelo CLIP (OpenAI)", num_top_classes=len(CATEGORIAS_CLIP))

    gr.Markdown("""
    ---
    **Detalles técnicos**
    - Modelo personalizado: Entrenado para frutas **maduras**, **verdes** y **podridas**
    - CLIP: Modelo generalista de OpenAI
    - Proyecto académico 2025 - *Procesamiento Digital de Imágenes y Visión por Computadora*
    """)

    boton_custom.click(fn=clasificar_con_custom, inputs=imagen_input, outputs=resultado_custom)
    boton_clip.click(fn=clasificar_con_clip, inputs=imagen_input, outputs=resultado_clip)

if __name__ == "__main__":
    demo.launch()
