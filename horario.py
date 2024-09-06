#defs
def nuevo(duracion, mes_inicio, dia_inicio, hora_inicio, minuto_inicio, dias_feb):
    def mes_escrito(mes_inicio):
        mes = mes_inicio
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
    
    def cambio_mes(mes_inicio, dias_feb, dia_final):
        if mes_inicio == 1 or mes_inicio == 3 or mes_inicio == 5 or mes_inicio == 7 or mes_inicio == 8 or mes_inicio == 10 or mes_inicio == 12:
            if dia_final > 31:
                mes_final = mes_inicio + 1
                dia_final = dia_final - 31
            else:
                mes_final = mes_inicio
        elif mes_inicio == 2:
            if dia_final > dias_feb:
                mes_final = mes_inicio + 1
                dia_final = dia_final - dias_feb
            else:
                mes_final = mes_inicio
        else:
            if dia_final > 30:
                mes_final = mes_inicio + 1
                dia_final = dia_final - 30
            else:
                mes_final = mes_inicio
        return(mes_final, dia_final)
    
    hora_en_minutos = hora_inicio*60
    horario = hora_en_minutos + minuto_inicio
    tiempo_f = horario + duracion
    hora_final = int(tiempo_f / 60)
    minuto_final = tiempo_f % 60
    dia_final = dia_inicio
    h = hora_inicio
    while hora_final >= 24:
        dia_final = int(dia_final + (hora_final / 24))
        hora_final = h + (hora_final % 24)
        if hora_final >= 24:
            h = 0
            
    mes_final, dia_final = cambio_mes(mes_inicio, dias_feb, dia_final)
    if mes_final > 12:
        mes_final = 1
    
    mes_inicio_letra = mes_escrito(mes_inicio)
    mes_final_letra = mes_escrito(mes_final)
    
    return(duracion, dia_inicio, mes_inicio_letra, hora_inicio, minuto_inicio, dia_final, mes_final_letra, hora_final, minuto_final)

#variables
def variables_nuevo():
    dias_feb = int(input("escribe 1 si es año biciesto o 2 si no lo es "))
    while dias_feb != 1 and dias_feb != 2:
        dias_feb = int(input("escribe un valor válido "))
    if dias_feb == 1:
        dias_feb = 29
    else:
        dias_feb = 28
    actividad = str(input("¿Qué actividad tienes pendiente? " ))
    duracion = int(input("¿Cuántos minutos dura? "))
    while duracion <=0:
        duracion = int(input("escribe un valor válido "))
    mes_inicio = int(input("¿Qué mes es? (expresa el mes en número) "))
    while mes_inicio <=0 or mes_inicio > 12:
        mes_inicio = int(input("escribe un valor válido "))
    dia_inicio = int(input("¿Qué día es? "))
    if mes_inicio == 1 or mes_inicio == 3 or mes_inicio == 5 or mes_inicio == 7 or mes_inicio == 8 or mes_inicio == 10 or mes_inicio == 12:
        while dia_inicio <= 0 or dia_inicio > 31:
            dia_inicio = int(input("escribe un valor válido "))
    elif mes_inicio == 2:
        while dia_inicio <= 0 or dia_inicio > dias_feb:
            dia_inicio = int(input("escribe un valor válido "))
    else:
        while dia_inicio <= 0 or dia_inicio > 30:
            dia_inicio = int(input("escribe un valor válido "))
    

    hora_inicio = int(input("¿A que hora inicia tu actividad?(expresa en hora militar) "))
    while hora_inicio >= 24 or hora_inicio < 0:
        hora_inicio = int(input("escribe un valor válido "))
    minuto_inicio = int(input("¿En que minuto de esa hora inicia tu actividad? "))
    while minuto_inicio >= 60 or minuto_inicio < 0:
        minuto_inicio = int(input("escribe un valor válido "))
    return(actividad, duracion, mes_inicio, dia_inicio, hora_inicio, minuto_inicio, dias_feb)

#main
accion = int(input("escribe 1 para agregar una actividad, 2 para desplegar actividades de un dia o 3 para eliminar una actividad "))
if accion == 1:
    actividad, duracion, mes_inicio, dia_inicio, hora_inicio, minuto_inicio, dias_feb = variables_nuevo()
    duracion, dia_inicio, mes_inicio_letra, hora_inicio, minuto_inicio, dia_final, mes_final_letra, hora_final, minuto_final = nuevo(duracion, mes_inicio, dia_inicio, hora_inicio, minuto_inicio, dias_feb)
    print(actividad, "dura", duracion, "minutos y es el", dia_inicio, "de", mes_inicio_letra, "a las", hora_inicio, ":", minuto_inicio, "y termina el", dia_final, "de", mes_final_letra, "a las", "%.0f" % (hora_final), ":", minuto_final)
elif accion == 2:
    pass
elif accion == 3:
    pass
else:
    while accion < 1 or accion > 3:
        accion = int(input("escribe un valor válido "))
