class SensorBiomedico:
    def __init__(self, id_sensor, tipo, unidad_medida):
        self.__id_sensor = id_sensor
        self.__tipo = tipo
        self.__unidad_medida = unidad_medida

    # Getters
    def get_id_sensor(self):
        return self.__id_sensor

    def get_tipo(self):
        return self.__tipo

    def get_unidad_medida(self):
        return self.__unidad_medida

    # Setters
    def set_id_sensor(self, id_sensor):
        self.__id_sensor = id_sensor

    def set_tipo(self, tipo):
        self.__tipo = tipo

    def set_unidad_medida(self, unidad_medida):
        self.__unidad_medida = unidad_medida

    def mostrar_datos(self):
        return {
            "ID": self.__id_sensor,
            "Tipo": self.__tipo,
            "Unidad": self.__unidad_medida
        }



class SensorCardiaco(SensorBiomedico):
    def __init__(self, id_sensor, tipo, unidad_medida, frecuencia_muestreo):
        super().__init__(id_sensor, tipo, unidad_medida)
        self.__frecuencia_muestreo = frecuencia_muestreo

    def get_frecuencia_muestreo(self):
        return self.__frecuencia_muestreo

    def set_frecuencia_muestreo(self, frecuencia_muestreo):
        self.__frecuencia_muestreo = frecuencia_muestreo

    def mostrar_datos(self):
        datos = super().mostrar_datos()
        datos["Frecuencia muestreo (Hz)"] = self.__frecuencia_muestreo
        return datos


class SensorRespiratorio(SensorBiomedico):
    def __init__(self, id_sensor, tipo, unidad_medida, capacidad_flujo):
        super().__init__(id_sensor, tipo, unidad_medida)
        self.__capacidad_flujo = capacidad_flujo

    def get_capacidad_flujo(self):
        return self.__capacidad_flujo

    def set_capacidad_flujo(self, capacidad_flujo):
        self.__capacidad_flujo = capacidad_flujo

    def mostrar_datos(self):
        datos = super().mostrar_datos()
        datos["Capacidad flujo (L/min)"] = self.__capacidad_flujo
        return datos


class SensorTemperatura(SensorBiomedico):
    def __init__(self, id_sensor, tipo, unidad_medida, rango_operacion):
        super().__init__(id_sensor, tipo, unidad_medida)
        self.__rango_operacion = rango_operacion

    def get_rango_operacion(self):
        return self.__rango_operacion

    def set_rango_operacion(self, rango_operacion):
        self.__rango_operacion = rango_operacion

    def mostrar_datos(self):
        datos = super().mostrar_datos()
        datos["Rango operación"] = self.__rango_operacion
        return datos


# Sistema de monitoreo
class SistemaMonitoreo:
    def __init__(self):
        self.sensores = []

    def agregar_sensor(self, sensor):
        for s in self.sensores:
            if s.get_id_sensor() == sensor.get_id_sensor():
                print("El sensor ya está registrado.")
                return
        self.sensores.append(sensor)
        print("Sensor agregado correctamente.")

    def ver_datos_sensor(self, id_sensor):
        for s in self.sensores:
            if s.get_id_sensor() == id_sensor:
                return s.mostrar_datos()
        return "⚠️ Sensor no encontrado."

    def contar_sensores(self):
        return len(self.sensores)


def main():
    sistema = SistemaMonitoreo()

    while True:
        print("\n--- SISTEMA DE MONITOREO ---")
        print("1. Agregar sensor")
        print("2. Ver datos de un sensor")
        print("3. Contar sensores")
        print("4. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            print("\nTipos de sensores:")
            print("a. Sensor Cardiaco")
            print("b. Sensor Respiratorio")
            print("c. Sensor Temperatura")
            tipo_sensor = input("Seleccione el tipo de sensor: ")

            id_sensor = input("ID del sensor: ")
            tipo = input("Tipo (ej. presión arterial, oxígeno, etc.): ")
            unidad = input("Unidad de medida: ")

            if tipo_sensor.lower() == "a":
                frecuencia = float(input("Frecuencia de muestreo (Hz): "))
                sensor = SensorCardiaco(id_sensor, tipo, unidad, frecuencia)

            elif tipo_sensor.lower() == "b":
                capacidad = float(input("Capacidad de flujo (L/min): "))
                sensor = SensorRespiratorio(id_sensor, tipo, unidad, capacidad)

            elif tipo_sensor.lower() == "c":
                minimo = float(input("Rango mínimo: "))
                maximo = float(input("Rango máximo: "))
                sensor = SensorTemperatura(id_sensor, tipo, unidad, (minimo, maximo))

            else:
                print("Tipo de sensor inválido.")
                continue

            sistema.agregar_sensor(sensor)

        elif opcion == "2":
            id_sensor = input("Ingrese el ID del sensor a consultar: ")
            datos = sistema.ver_datos_sensor(id_sensor)
            print("Datos del sensor:", datos)

        elif opcion == "3":
            print("Total de sensores registrados:", sistema.contar_sensores())

        elif opcion == "4":
            print("👋 Saliendo del sistema...")
            break

        else:
            print("Opción inválida, intente de nuevo.")


if __name__ == "__main__":
    main()
