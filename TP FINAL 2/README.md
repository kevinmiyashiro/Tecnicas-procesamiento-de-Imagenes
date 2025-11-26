---
title: Restaurador De Recuerdos IA
emoji: ✨
colorFrom: indigo
colorTo: purple
sdk: streamlit
sdk_version: 1.39.0
app_file: app.py
pinned: false
license: mit
---

# ✨ Restaurador de Recuerdos IA

> Una herramienta impulsada por IA generativa para recuperar, mejorar y analizar fotografías antiguas o de baja calidad.

[![Hugging Face Spaces](https://img.shields.io/badge/🤗%20Hugging%20Face-Open%20Space-blue)](https://huggingface.co/spaces/[TU_USUARIO]/[TU_ESPACIO])
[![Python](https://img.shields.io/badge/Python-3.9+-yellow)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.39-red)](https://streamlit.io/)

## 📝 Descripción

Este proyecto es un **Producto Mínimo Viable (MVP)** desarrollado como Trabajo Integrador Final para la materia de *Procesamiento Digital de Imágenes*. 

El sistema permite a usuarios no técnicos restaurar fotografías degradadas, borrosas o antiguas utilizando modelos de difusión y GANs de última generación (GFPGAN y Real-ESRGAN). Además, integra un módulo de visión por computadora (CLIP) que analiza y valida técnicamente la mejora de la imagen, ofreciendo una comparación interactiva del antes y el después.

## 👤 User Persona

El diseño de esta aplicación se centra en **Laura**:

* **Perfil:** 50 años, aficionada a la genealogía y guardiana del archivo familiar.
* **Contexto:** Tiene cajas de fotos antiguas escaneadas y fotos digitales de los 2000 que se ven pixeladas en pantallas modernas. No tiene conocimientos técnicos de edición.
* **Problema:** "Quiero compartir las fotos de mis abuelos en el grupo familiar, pero se ven borrosas y las caras no se distinguen bien. Los programas profesionales son muy difíciles de usar."
* **Solución:** Una web simple donde arrastra la foto y la IA reconstruye los rostros automáticamente en segundos.

## 🚀 Demo

Puedes probar la aplicación en vivo aqui https://huggingface.co/spaces/kevinmiyashiro/tpfinal

## ✨ Características Principales

* **Restauración de Rostros:** Utiliza GFPGAN para reconstruir rasgos faciales perdidos en fotos antiguas.
* **Super-Resolución (Upscaling):** Aumenta la resolución (x2, x4) manteniendo la nitidez con Real-ESRGAN.
* **Análisis de Calidad Visual:** Implementación local de **CLIP (OpenAI)** para clasificar semánticamente la calidad de la imagen (ej: detectar si pasó de "borrosa" a "nítida").
* **Comparación Interactiva:** Slider visual para comparar pixel a pixel el resultado.
* **Interfaz Simple:** Diseñada en Streamlit pensando en la usabilidad para usuarios no técnicos.

## 🛠️ Stack Tecnológico

**Frontend & UI:**
* **Streamlit:** Para la creación de la interfaz web interactiva.

**Modelos de IA (Pipeline Híbrido):**
* **Generación (Nube):** GFPGAN y Real-ESRGAN ejecutados vía API de **Replicate** (para evitar saturar la memoria del entorno gratuito).
* **Análisis (Local):** Modelo `openai/clip-vit-base-patch32` ejecutado localmente con **Hugging Face Transformers**.

**Procesamiento:**
* **Pillow (PIL):** Manipulación básica de imágenes.
* **NumPy:** Manejo de arrays para la comparación visual.

**Despliegue:**
* **Hugging Face Spaces:** Hosting de la aplicación.

## 🏗️ Arquitectura del Sistema

```mermaid
graph LR
    A[Usuario] -->|Sube Imagen| B(Streamlit UI)
    B -->|Envía a Procesar| C{Replicate API}
    C -->|Rostros| D[GFPGAN]
    C -->|General| E[Real-ESRGAN]
    D & E -->|Imagen Restaurada| F[Backend Local]
    F -->|Análisis de Calidad| G[Modelo CLIP]
    G -->|Resultados + Comparación| B