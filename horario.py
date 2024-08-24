def nuevo(actividad, duracion, mes, dia):
    if mes == 1:
        mes_letra = "enero"
    elif mes == 2:
        mes_letra = "febrero"
    elif mes == 3:
        mes_letra = "marzo"
    elif mes == 4:
        mes_letra = "abril"
    elif mes == 5:
        mes_letra = "mayo"
    elif mes == 6:
        mes_letra = "junio"
    elif mes == 7:
        mes_letra = "julio"
    elif mes == 8:
        mes_letra = "agosto"
    elif mes == 9:
        mes_letra = "septiembre"
    elif mes == 10:
        mes_letra = "octubre"
    elif mes == 11:
        mes_letra = "noviembre"
    elif mes == 12:
        mes_letra = "diciembre"
    else:
        mes_letra = "indefinido"
    agendar = (actividad, duracion, mes, dia)
    resultado = actividad, "dura", duracion, "minutos, es el", dia, "de ", mes_letra
    return resultado

actividad = str(input("¿Qué actividad tienes pendiente? " ))
duracion = int(input("¿Cuántos minutos dura? "))
mes = int(input("¿Qué mes es? (expresa el mes en número) "))
dia = int(input("¿Qué día es? "))

print(nuevo(actividad, duracion, mes, dia))
