import gradio as gr
import cv2
import numpy as np
from utils import resize_max, preset_cleanup, preset_revive, preset_sharp, denoise_fastnlmeans, apply_clahe, unsharp_mask, bilateral_filter
from PIL import Image

def bgr_to_pil(bgr_img):
    rgb = cv2.cvtColor(bgr_img, cv2.COLOR_BGR2RGB)
    return Image.fromarray(rgb)

def pil_to_bgr(pil_img):
    rgb = np.array(pil_img)
    return cv2.cvtColor(rgb, cv2.COLOR_RGB2BGR)

def process_image(pil_img, preset, denoise_h, clahe_clip, unsharp_amount, show_steps):
    img_bgr = pil_to_bgr(pil_img)
    img_bgr = resize_max(img_bgr, max_dim=1024)

    if preset == 'Limpieza':
        out = preset_cleanup(img_bgr)
    elif preset == 'Revive':
        out = preset_revive(img_bgr)
    elif preset == 'Nítido':
        out = preset_sharp(img_bgr)
    else:
        out = img_bgr.copy()

    if denoise_h > 0:
        out = denoise_fastnlmeans(out, h=int(denoise_h), hColor=int(denoise_h))
    if clahe_clip > 0:
        out = apply_clahe(out, clipLimit=float(clahe_clip))
    if unsharp_amount > 0:
        out = unsharp_mask(out, amount=float(unsharp_amount))

    return bgr_to_pil(img_bgr), bgr_to_pil(out)

with gr.Blocks() as demo:
    gr.Markdown("# ImageEnhancer — TP Procesamiento de Imágenes")
    with gr.Row():
        img_in = gr.Image(type="pil", label="Imagen original")
    with gr.Row():
        preset = gr.Radio(["Limpieza","Revive","Nítido","Ninguno"], value="Revive", label="Preset")
        denoise_h = gr.Slider(0, 20, value=0, label="Denoise h")
        clahe_clip = gr.Slider(0.0, 5.0, value=0.0, step=0.1, label="CLAHE clip")
        unsharp_amount = gr.Slider(0.0, 2.0, value=0.0, step=0.1, label="Unsharp amount")
        show_steps = gr.Checkbox(label="Mostrar steps")
        btn = gr.Button("Procesar")
    out1 = gr.Image(label="Original procesada")
    out2 = gr.Image(label="Procesada final")

    btn.click(process_image, [img_in, preset, denoise_h, clahe_clip, unsharp_amount, show_steps], [out1, out2])

if __name__ == '__main__':
    demo.launch(server_name='0.0.0.0')
