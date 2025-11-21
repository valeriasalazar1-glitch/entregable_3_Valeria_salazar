from procesador import ProcesadorDICOM

def main():
    procesador = ProcesadorDICOM(ruta_directorio='dicoms', descargar_pruebas=True)

    procesador.cargar_archivos()
    procesador.extraer_metadatos()
    procesador.calcular_intensidad_promedio()

    print('Resultados')
    print(procesador.dataframe.head())

    procesador.guardar_csv('resultados_dicom.csv')

    print('Fin del proceso')


if __name__ == "__main__":
    main()
