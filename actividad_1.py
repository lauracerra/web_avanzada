def calcular_tarifa_estacionamiento(horas_estacionadas, minutos_estacionados, dia):
    if dia in ["lunes", "martes", "miércoles"]:
        tarifa_hora = 2.00
    elif dia in ["jueves", "viernes"]:
        tarifa_hora = 2.50
    elif dia in ["sábado", "domingo"]:
        tarifa_hora = 3.00
    else:
        print("Día de la semana incorrecto")
        return

    tiempo_total = horas_estacionadas + minutos_estacionados / 60

    if minutos_estacionados % 5 != 0:
        tiempo_total = round(tiempo_total) + 1

    total_pagar = tarifa_hora * tiempo_total
    print(f"Total a pagar: ${total_pagar:.2f}")

# Entrada de datos
horas_estacionadas = int(input("Ingrese las horas estacionadas: "))
minutos_estacionados = int(input("Ingrese los minutos estacionados: "))
dia_semana = input("Ingrese el día de la semana: ").lower()

calcular_tarifa_estacionamiento(horas_estacionadas, minutos_estacionados, dia_semana)

