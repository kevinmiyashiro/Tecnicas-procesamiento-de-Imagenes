---
title: Clasificador de frutas frescas, verdes y podridas
emoji: 🍌
colorFrom: green
colorTo: yellow
sdk: gradio
sdk_version: 4.44.0
app_file: app.py
pinned: false
---

## 🧩 Desarrollo

Proyecto desarrollado para la materia **Procesamiento Digital de Imágenes y Visión por Computadora**.

**Autor:** Kevin Miyashiro  
**Año:** 2025  
**Institución:** IFTS24

---

# 🍎 Clasificador de Frutas (Frescas, Verdes y Podridas)

## 🧠 Descripción

Esta aplicación utiliza un modelo de inteligencia artificial entrenado con **Teachable Machine** para clasificar imágenes de frutas según su estado de maduración.  
Podés subir una foto de una fruta (por ejemplo, banana, manzana o naranja) y el sistema detectará si está **verde**, **madura** o **podrida**.  

Ideal para proyectos de visión por computadora, control de calidad o aprendizaje automático básico.

---

## 🤖 Modelo utilizado

- **Modelo personalizado**: `keras_model.h5` (entrenado en [Teachable Machine](https://teachablemachine.withgoogle.com/))  
- **Tarea**: Clasificación de imágenes (3 clases)
- **Framework**: TensorFlow / Keras
- **Interfaz**: Gradio

---

## 🏷️ Categorías detectadas

El modelo puede clasificar imágenes en las siguientes clases:

1. 🍏 **Fruta verde** – Aún sin madurar.  
2. 🍎 **Fruta madura** – Lista para consumir.  
3. 🤢 **Fruta podrida** – En mal estado o no apta para consumo.  

---

## 🚀 Cómo usar

1. Subí una imagen de una fruta o utilizá la cámara desde el navegador.  
2. Presioná el botón **"Clasificar"**.  
3. Esperá unos segundos y mirá el resultado, que mostrará la categoría detectada junto con el nivel de confianza.  

> 💡 Tip: Cuanto más clara y enfocada sea la imagen, mejor será la precisión del modelo.

---

## Modelo Preentrenado (CLIP)

## Ventajas:

-No requiere entrenamiento.
-Funciona con cualquier categoría en lenguaje natural.
-Generaliza bien a diferentes contextos.

## Desventajas:

-Menor precisión en tareas específicas.
-No se adapta al dominio particular de frutas.
-Resultados en mi dataset:

Precisión aproximada: 65-75%
Funciona mejor en frutas claramente maduras o podridas, pero suele confundirse con frutas verdes sin madurar porque no fue entrenado específicamente en este dataset.


## Modelo personalizado (Teachable Machine, 3 clases × 300 imágenes)

##Ventajas:

-Alta precisión en la tarea específica de frutas.
-Adaptado al dominio de interés.
-Más rápido en inferencia.

## Desventajas:

-Requiere recolectar y etiquetar datos.
-Solo funciona para las clases entrenadas.
-Puede sufrir overfitting si hay pocas imágenes.

Precisión aproximada: 90 – 95 %

Muy buena para todas las clases, especialmente si las imágenes de entrenamiento son variadas y de buena calidad.


## Cómo usar

Subí una imagen o usá tu cámara.
Presioná "Clasificar con Modelo Personalizado" o "Clasificar con CLIP".
Observá los resultados de ambas predicciones lado a lado.

## 🛠️ Instalación local

Si querés ejecutar el proyecto localmente:

```bash
# Clonar el repositorio
git clone https://huggingface.co/spaces/kevinmiyashiro/proyecto_computer_vision
cd proyecto_computer_vision

# Crear entorno virtual
python -m venv venv
# En Windows:
venv\Scripts\activate
# En Linux/Mac:
source venv/bin/activate

# Instalar dependencias
pip install -r requirements.txt

# Ejecutar aplicación
python app.py


## Conclusiones

Elección de modelos: Los modelos preentrenados como CLIP son útiles para prototipos rápidos o cuando no se dispone de un dataset propio; permiten clasificar imágenes en categorías generales sin entrenamiento adicional. Sin embargo, para tareas específicas y dominios particulares —como clasificar frutas maduras, verdes o podridas—, los modelos personalizados ofrecen mayor precisión y confiabilidad.

Aprendizaje del proceso: Crear un modelo personalizado nos permitió entender todo el flujo: recopilación y etiquetado de imágenes, entrenamiento con Teachable Machine, preprocesamiento de imágenes y despliegue en una aplicación con Gradio. Aprendimos también a comparar resultados y a evaluar fortalezas y limitaciones de cada enfoque.

Posibles mejoras:

Aumentar la cantidad y diversidad de imágenes por clase para reducir overfitting y mejorar la generalización.

Aplicar técnicas de data augmentation (rotación, brillo, zoom) para robustecer el modelo.

Entrenar un modelo más complejo o usar fine-tuning de modelos preentrenados como MobileNet o EfficientNet para mejorar aún más la precisión.

Implementar alertas o recomendaciones en la app según la categoría detectada.

Aplicaciones reales: Este proyecto puede aplicarse en la industria alimentaria para clasificar frutas automáticamente, en supermercados para controlar calidad, o en huertas para separar fruta madura de la no lista para venta. También es útil como base educativa para aprender visión por computadora y despliegue de modelos de IA.