import os
import pydicom
import pandas as pd
import numpy as np


class ProcesadorDICOM:
    def __init__(self, ruta_directorio):
        self.ruta = ruta_directorio
        self.archivos_dicom = []
        self.dataframe = None 
        
    def cargar_archivos(self):
        print('buscando en directorio:', self.ruta)
        for archivo in os.listdir(self.ruta):
            ruta_archivo = os.path.join(self.ruta, archivo)

            try:
                dicom = pydicom.dcmread(ruta_archivo)
                self.archivos_dicom.append(dicom)
            except Exception:
                print(f'No es un archivo DICOM válido: {archivo}')

        print(f'Total de archivos DICOM cargados: {len(self.archivos_dicom)}')

    def extraer_metadatos(self):
        registros = []

        for dicom in self.archivos_dicom:
            datos = {
                'PatientID': getattr(dicom, 'PatientID', None),
                'PatientName': getattr(dicom, 'PatientName', None),
                'StudyInstanceUID': getattr(dicom, 'StudyInstanceUID', None),
                'StudyDescription': getattr(dicom, 'StudyDescription', None),
                'StudyDate': getattr(dicom, 'StudyDate', None),
                'Modality': getattr(dicom, 'Modality', None),
                'Rows': getattr(dicom, 'Rows', None),
                'Columns': getattr(dicom, 'Columns', None),
            }
            registros.append(datos)

        self.dataframe = pd.DataFrame(registros)
        print('\nMetadatos extraídos correctamente')
        return self.dataframe

    def calcular_intensidad_promedio(self):
        intensidades = []

        for dicom in self.archivos_dicom:
            try:
                pixel_array = dicom.pixel_array
                intensidad_media = np.mean(pixel_array)
            except Exception:
                intensidad_media = None

            intensidades.append(intensidad_media)

        self.dataframe['IntensidadPromedio'] = intensidades
        print('Columna "IntensidadPromedio" añadida correctamente')

        return self.dataframe
