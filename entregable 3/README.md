# Taller – Introducción a la Informática Médica  
## Valeria Salazar Ibargüen

## 1. Descripción del proyecto

Este proyecto implementa una aplicación en Python para cargar, analizar y extraer información de archivos DICOM, simulando parte del funcionamiento de un sistema utilizado en entornos hospitalarios.  
- Carga archivos DICOM desde un directorio.
- Extraer metadatos esenciales (ID del paciente, modalidad, fecha, tamaño, etc.).
- Calcula la intensidad promedio de las imágenes.
- Genera un archivo CSV con los resultados.

El sistema está desarrollado usando POO mediante la clase `ProcesadorDICOM`.


## 2. Por qué DICOM y HL7 son esenciales en salud

### DICOM
Es el estándar internacional usado para almacenar, transmitir y visualizar imágenes médicas (TAC, RM, RX).  
Incluye tanto la imagen como los metadatos clínicos necesarios para interpretarla.  
Permite la interoperabilidad entre equipos de diferentes fabricantes.

### HL7
Es el estándar utilizado para el intercambio de información clínica estructurada:

- Datos del paciente
- Laboratorio
- Órdenes médicas
- Historia clínica

### Diferencia conceptual
DICOM 
- Se usa para imágenes médicas 
- Contiene píxeles + metadatos 
- Es clave en sistemas PACS (usa DICOM y HL7 para integrar imagen y datos del paciente) 

HL7:
- Se usa para datos clínicos
- Contiene solo informacion en texto
- Se usa en HIS y EHR

Ambos estándares son complementarios para lograr una comunicación interoperable en el sistema de salud.

## 3. Relevancia clínica del análisis de intensidades

Analizar la distribución de intensidades en una imagen médica permite:

- Identificar tejidos según su rango de intensidades
- Detectar artefactos o errores de adquisición
- Evaluar la calidad del estudio
- Preparar la imagen para segmentación o machine learning
- Comparar progresión clínica entre estudios del mismo paciente

Es una etapa fundamental del preprocesamiento en radiología computacional.


## 4. Dificultades encontradas

- Algunos DICOM vienen anonimizados y no contienen ciertos tags.
- Diferentes modalidades tienen formatos de pixel_array distintos.
- Algunos archivos requieren `force=True` para leerse.
- La estandarización entre fabricantes puede generar variaciones.

Python y librerías como pydicom, numpy y pandas facilitan el trabajo con grandes volúmenes de imágenes y metadatos, imitando flujos reales de un PACS.

