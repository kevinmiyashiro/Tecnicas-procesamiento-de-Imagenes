# Proyecto: Image Enhancer – Mejora de Imágenes con Técnicas de Procesamiento Digital

**Año lectivo:** 2025  
**Instituto:** IFTS24  
**Materia:** Procesamiento de Imágenes  
**Profesor:** Matías Barreto  
**Alumno:** Kevin Miyashiro

---

## 📌 Descripción del Proyecto
Este proyecto consiste en el desarrollo de una aplicación interactiva llamada **Image Enhancer**, creada para aplicar diferentes técnicas de **procesamiento digital de imágenes** utilizando Python y librerías especializadas. La aplicación permite mejorar imágenes mediante filtros como reducción de ruido, realce de bordes, aumento de contraste y nitidez, entre otros.

El objetivo principal es demostrar la implementación práctica de técnicas vistas en la materia, integrarlas en un sistema funcional y desplegarlo en **Hugging Face Spaces** utilizando **Gradio** como interfaz.

---

## 🎯 Objetivo General
Aplicar técnicas de procesamiento digital de imágenes para desarrollar una herramienta interactiva que permita mejorar fotografías mediante filtros clásicos y avanzados, demostrando comprensión teórica y práctica de los contenidos de la materia.

---

## 🎯 Objetivos Específicos
- Implementar filtros como **CLAHE**, **Denoising**, **Sharpening**, **Equalización de histograma**, entre otros.
- Desarrollar una interfaz web sencilla y funcional utilizando **Gradio**.
- Integrar las funciones de procesamiento en un flujo completo de carga, transformación y visualización de imágenes.
- Desplegar el proyecto en Hugging Face para demostrar su utilidad real.
- Documentar el proceso, decisiones técnicas y aprendizajes obtenidos.

---

## 🧰 Tecnologías Utilizadas
- **Python 3.10+**
- **OpenCV (cv2)** — Procesamiento de imágenes
- **scikit-image** — Cálculo de métricas (PSNR/SSIM)
- **Pillow (PIL)** — Manejo de imágenes
- **NumPy** — Operaciones matriciales
- **Gradio** — Interfaz visual para la aplicación
- **Hugging Face Spaces** — Hosting del proyecto

---

## 🖼️ ¿Para qué sirve esta aplicación?
La herramienta **Image Enhancer** permite:

- Mejorar la calidad visual de fotografías con ruido o poca nitidez.  
- Realzar bordes y detalles.
- Aumentar el contraste en zonas oscuras mediante **CLAHE**.
- Explorar visualmente cómo afectan los filtros a una imagen.
- Comprender el funcionamiento real de técnicas fundamentales del procesamiento digital.

Es una app práctica tanto para estudiantes como para cualquier usuario que quiera mejorar rápidamente una imagen.

---

## ⚙️ ¿Cómo funciona?
1. El usuario carga una imagen (PNG o JPG).
2. Elige un filtro del menú desplegable.
3. Si el filtro lo permite, ajusta parámetros (intensidad, tamaño del kernel, etc.).
4. La aplicación procesa la imagen usando las funciones implementadas en `utils.py`.
5. Se muestra la imagen original junto con la imagen filtrada.
6. El usuario puede descargar el resultado.

La interfaz está construida con **Gradio**, lo que permite una experiencia clara e intuitiva.

---

## 🧠 Técnicas de Procesamiento Utilizadas
### ✔️ Reducción de ruido (Denoise)
- Basado en **fastNlMeansDenoisingColored**
- Suaviza la imagen preservando bordes

### ✔️ Sharpening (Unsharp Mask)
- Genera una versión suavizada
- Resta esa versión a la original para reforzar bordes

### ✔️ CLAHE (Contrast Limited Adaptive Histogram Equalization)
- Mejora el contraste local
- Útil en imágenes subexpuestas

### ✔️ Edge Enhancement
- Resalta contornos mediante kernels de convolución

### ✔️ Equalización de histograma
- Mejora niveles de intensidad de toda la imagen

### ✔️ Grayscale y filtros artísticos
- Convierte imágenes a escala de grises
- Emboss y filtros similares

---

## 📊 Métricas Implementadas
En el notebook del proyecto también se calculan métricas:
- **PSNR (Peak Signal-to-Noise Ratio)**
- **SSIM (Structural Similarity Index)**

Estas permiten evaluar la calidad del procesamiento comparando la imagen original con la mejorada.

---

## 📚 ¿Qué se aprendió en este trabajo?
- Cómo manipular imágenes digitalmente usando Python.
- Aplicación real de conceptos como convolución, histogramas y kernels.
- Implementación de filtros clásicos y modernos.
- Integración de algoritmos en una aplicación interactiva.
- Importancia de las métricas de calidad (PSNR/SSIM).
- Uso de herramientas modernas de despliegue como Hugging Face Spaces.
- Buenas prácticas de documentación y organización de proyectos.

---

## 🚀 Deploy en Hugging Face
La app fue diseñada para funcionar sin problemas en Spaces. Solo requiere:
- `app.py` como punto de entrada
- `utils.py` con las funciones de filtros
- `requirements.txt` para dependencias

La plataforma reconstruye la app automáticamente en cada push.

---

## 📎 Archivos incluidos
- `app.py` — Interfaz Gradio
- `utils.py` — Filtros y funciones de procesamiento
- `requirements.txt` — Dependencias
- `README.md` — Documentación del proyecto
- `notebook.ipynb` — Código experimental y métricas
- `informe_final.pdf` — Informe académico final

---

## 🏁 Conclusión
Este proyecto integra teoría y práctica del **Procesamiento Digital de Imágenes**, aplicando filtros fundamentales, evaluando resultados y ofreciendo una aplicación interactiva lista para usar y presentar. El trabajo refleja el desarrollo de habilidades técnicas, analíticas y de despliegue, cumpliendo completamente el objetivo académico propuesto.

---

Si necesitás agregar una sección extra para tu entrega, formatearlo diferente o generar una versión en PDF, avisame y te lo preparo.

