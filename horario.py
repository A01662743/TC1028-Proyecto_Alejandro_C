def nuevo(mes):
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
    return(mes_letra)

def horario(hora, minuto):
    hora_en_minutos = hora*60
    horario = hora_en_minutos + minuto
    return(horario)

def tiempo_final(hora_inicio, minuto_inicio, duracion, dia_inicio, mes_inicio):
    tiempo_f = horario(hora_inicio, minuto_inicio) + duracion
    hora_final = tiempo_f / 60
    minuto_final = tiempo_f % 60
    if hora_final > 24:
        dia_final = dia_inicio + 1
        hora_final = 0
        if dia_final > 31:
            mes_final = mes_inicio + 1
            dia_final = 1
            if mes_final > 12:
                mes_final = 1
        else:
            mes_final = mes_inicio
    else:
        dia_final = dia_inicio
        mes_final = mes_inicio
    return(hora_final, minuto_final, dia_final, mes_final)

actividad = str(input("¿Qué actividad tienes pendiente? " ))
duracion = int(input("¿Cuántos minutos dura? "))
while duracion <=0:
    duracion = int(input("escribe un valor válido "))
mes_inicio = int(input("¿Qué mes es? (expresa el mes en número) "))
while mes_inicio <=0 or mes_inicio > 12:
    mes_inicio = int(input("escribe un valor válido "))
dia_inicio = int(input("¿Qué día es? "))
while dia_inicio <=0 or dia_inicio > 31:
    dia_inicio = int(input("escribe un valor válido "))

hora_inicio = int(input("¿A que hora inicia tu actividad?(expresa en hora militar) "))
while hora_inicio >= 24 or hora_inicio < 0:
    hora_inicio = int(input("escribe un valor válido "))
if hora_inicio != 24:
    minuto_inicio = int(input("¿En que minuto de esa hora inicia tu actividad? "))
    while minuto_inicio >= 60 or minuto_inicio < 0:
        minuto_inicio = int(input("escribe un valor válido "))
else:
    minuto_inicio = 0

mes_inicio_letra = nuevo(mes_inicio)
hora_final, minuto_final, dia_final, mes_final = tiempo_final(hora_inicio, minuto_inicio, duracion, dia_inicio, mes_inicio)
mes_final = nuevo(mes_final)
print(actividad, "dura", duracion, "minutos y es el", dia_inicio, "de", mes_inicio_letra, "a las", hora_inicio, ":", minuto_inicio, "y termina el", dia_final, "de", mes_final, "a las", "%.0f" % (hora_final), ":", minuto_final)
