from procesador import ProcesadorDICOM

def main():
    ruta = 'dicoms'   

    procesador = ProcesadorDICOM(ruta)
    
    procesador.cargar_archivos()
    df = procesador.extraer_metadatos()
    df = procesador.calcular_intensidad_promedio()

    print('dataframe final')
    print(df)

    df.to_csv('esultados_dicom.csv', index=False)
    print("\nArchivo 'resultados_dicom.csv' generado.")


if __name__ == '__main__':
    main()
