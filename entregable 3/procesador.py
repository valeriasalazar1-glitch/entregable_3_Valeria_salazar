import os
import shutil
from typing import List, Optional
import pydicom
import pydicom.data
import pandas as pd
import numpy as np


class ProcesadorDICOM:
    """
    Clase para descargar archivos de prueba, cargar DICOMs, extraer metadatos
    y realizar análisis básico de intensidad de imagen.
    """

    def __init__(self, ruta_directorio: str = 'dicoms', descargar_pruebas: bool = True):
    
        self.ruta = ruta_directorio
        self.archivos_dicom: List[pydicom.dataset.FileDataset] = []
        self.dataframe: Optional[pd.DataFrame] = None

        os.makedirs(self.ruta, exist_ok=True)

        if descargar_pruebas:
            self._copiar_dicoms_de_prueba()

    def _copiar_dicoms_de_prueba(self):
      
        try:
            archivos_prueba = pydicom.data.get_testdata_files()
        except Exception as e:
            print('Error obteniendo archivos de prueba:', e)
            return

        copiados = 0
        for ruta_archivo in archivos_prueba:
            nombre = os.path.basename(ruta_archivo)
            destino = os.path.join(self.ruta, nombre)

            try:
                if not os.path.exists(destino):
                    shutil.copy(ruta_archivo, destino)
                    copiados += 1
            except Exception as e:
                print(f'[Aviso] Error copiando archivo {nombre}: {e}')

        print(f'Archivos de prueba copiados: {copiados}')


    def cargar_archivos(self):
        """
        Escanea la carpeta y carga solo archivos DICOM válidos.
        """
        archivos = sorted(os.listdir(self.ruta))
        cargados = 0
        self.archivos_dicom = []

        for nombre in archivos:
            ruta_archivo = os.path.join(self.ruta, nombre)
            if os.path.isdir(ruta_archivo):
                continue

            try:
                ds = pydicom.dcmread(ruta_archivo)
                self.archivos_dicom.append(ds)
                cargados += 1
            except Exception:
                print(f'No es un archivo DICOM valido: {nombre}')

        print(f'Total de archivos DICOM cargados: {cargados}')

    def extraer_metadatos(self):
        """
        Extrae los tags requeridos y crea un DataFrame.
        """
        registros = []

        for ds in self.archivos_dicom:
            registro = {
                'PatientID': getattr(ds, 'PatientID', None),
                'PatientName': getattr(ds, 'PatientName', None),
                'StudyInstanceUID': getattr(ds, 'StudyInstanceUID', None),
                'StudyDescription': getattr(ds, 'StudyDescription', None),
                'StudyDate': getattr(ds, 'StudyDate', None),
                'Modality': getattr(ds, 'Modality', None),
                'Rows': getattr(ds, 'Rows', None),
                'Columns': getattr(ds, 'Columns', None),
            }
            registros.append(registro)

        self.dataframe = pd.DataFrame(registros)
        print('Metadatos extraídos correctamente.')
        return self.dataframe
    
    def calcular_intensidad_promedio(self):
        if self.dataframe is None:
            self.extraer_metadatos()

        intensidades = []

        for ds in self.archivos_dicom:
            try:
                pixel_array = ds.pixel_array
                intensidad = float(np.mean(pixel_array))
            except Exception:
                intensidad = None

            intensidades.append(intensidad)

        self.dataframe['IntensidadPromedio'] = intensidades
        print('Intensidad promedio calculada.')
        return self.dataframe

    def guardar_csv(self, salida='resultados_dicom.csv'):
        if self.dataframe is not None:
            self.dataframe.to_csv(salida, index=False)
            print(f'Archivo guardado como "{salida}".')
        else:
            print('No hay DataFrame para guardar')
