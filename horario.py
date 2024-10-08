#variables globales/constantes
meses_con_31 = list([1, 3, 5, 7, 8, 10, 12])
biblioteca_temp = {}
biblioteca_general = {}

#defs

#dias en febrero
def bisciesto(año):
    if año%4 == 0:
        if año%100 == 0:
            if año%400 == 0:
                dias_feb = 29
            else:
                dias_feb = 28
        else:
            dias_feb = 29
    else:
        dias_feb = 28
    return(dias_feb)

#mes en letra
def mes_escrito(mes):
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

#opcion 1
def nuevo():
    global dias_feb
    
    def variables_nuevo():
        actividad = str(input("¿Qué actividad tienes pendiente? " ))
        duracion = int(input("¿Cuántos minutos dura? "))
        while duracion <=0:
            duracion = int(input("escribe un valor válido "))
        mes_inicio = int(input("¿Qué mes es? (expresa el mes en número) "))
        while mes_inicio <=0 or mes_inicio > 12:
            mes_inicio = int(input("escribe un valor válido "))
        dia_inicio = int(input("¿Qué día es? "))
        if mes_inicio in meses_con_31:
            while dia_inicio <= 0 or dia_inicio > 31:
                dia_inicio = int(input("escribe un valor válido "))
        elif mes_inicio == 2:
            while dia_inicio <= 0 or dia_inicio > dias_feb:
                dia_inicio = int(input("escribe un valor válido "))
        else:
            while dia_inicio <= 0 or dia_inicio > 30:
                dia_inicio = int(input("escribe un valor válido "))
    
        hora_inicio = int(input("¿A que hora inicia tu actividad?(expresa en hora militar sin los minutos) "))
        while hora_inicio >= 24 or hora_inicio < 0:
            hora_inicio = int(input("escribe un valor válido "))
        minuto_inicio = int(input("¿En que minuto de esa hora inicia tu actividad? "))
        while minuto_inicio >= 60 or minuto_inicio < 0:
            minuto_inicio = int(input("escribe un valor válido "))
        return(actividad, duracion, mes_inicio, dia_inicio, hora_inicio, minuto_inicio)
    
    def cambio_mes(mes_inicio, dias_feb, dia_final):
        mes_final = mes_inicio
        while ((mes_final in meses_con_31) and dia_final > 31) or (mes_final == 2 and dia_final > dias_feb) or ((mes_final not in meses_con_31 and mes_final != 2) and dia_final > 30):
            if mes_final in meses_con_31:
                if mes_final == 12:
                    mes_final = 1
                else:
                    mes_final = mes_final + 1
                dia_final = dia_final - 31
            elif mes_final == 2:
                mes_final = mes_final + 1
                dia_final = dia_final - dias_feb
            elif mes_final not in meses_con_31 and mes_final != 2:
                mes_final = mes_final + 1
                dia_final = dia_final - 30
        return(mes_final, dia_final)
    
    def guardar(actividad, duracion, dia_inicio, mes_inicio_letra, hora_inicio, minuto_inicio, dia_final, mes_final_letra, hora_final, minuto_final):
        global biblioteca_temp
        global biblioteca_general
        biblioteca_temp[dia_inicio] = {"actividad" : [actividad],
                        "duracion" : [duracion],
                        "dia_inicio" : [dia_inicio],
                        "mes_inicio_letra" : [mes_inicio_letra],
                        "hora_inicio" : [hora_inicio],
                        "minuto_inicio" : [minuto_inicio],
                        "dia_final" :[dia_final],
                        "mes_final_letra" : [mes_final_letra],
                        "hora_final" : [hora_final],
                        "minuto_final" : [minuto_final]}
        if biblioteca_general.get(mes_inicio_letra, {}).get(dia_inicio):
            for x in biblioteca_temp[dia_inicio].keys():
                biblioteca_temp[dia_inicio][x] = biblioteca_temp[dia_inicio][x][0]
                biblioteca_general[mes_inicio_letra][dia_inicio][x].append(biblioteca_temp[dia_inicio][x])
            biblioteca_temp = {}
        elif biblioteca_general.get(mes_inicio_letra) == None:
            biblioteca_general[mes_inicio_letra] = biblioteca_temp
            biblioteca_temp = {}
        else:
            biblioteca_general[mes_inicio_letra][dia_inicio] = biblioteca_temp[dia_inicio]
            biblioteca_temp = {}
    
    actividad, duracion, mes_inicio, dia_inicio, hora_inicio, minuto_inicio = variables_nuevo()
    
    hora_en_minutos = hora_inicio*60
    horario = hora_en_minutos + minuto_inicio
    tiempo_f = horario + duracion
    hora_final = int(tiempo_f / 60)
    minuto_final = tiempo_f % 60
    dia_final = dia_inicio
    dia_final = int(dia_final + (hora_final / 24))
    while hora_final > 24:
        hora_final = hora_final % 24
        if hora_final == 24:
            hora_final = 0
            
    mes_final, dia_final = cambio_mes(mes_inicio, dias_feb, dia_final)
    mes_inicio_letra = mes_escrito(mes_inicio)
    mes_final_letra = mes_escrito(mes_final)
    guardar(actividad, duracion, dia_inicio, mes_inicio_letra, hora_inicio, minuto_inicio, dia_final, mes_final_letra, hora_final, minuto_final)
    
    return(actividad, duracion, dia_inicio, mes_inicio_letra, hora_inicio, minuto_inicio, dia_final, mes_final_letra, hora_final, minuto_final)

#opcion 2
def recall(mes_pedido, dia_pedido):
    while True:
        mes_pedido_letra = mes_escrito(mes_pedido)
        if biblioteca_general.get(mes_pedido_letra, {}).get(dia_pedido) != None:
            return(biblioteca_general[mes_pedido_letra][dia_pedido], len(biblioteca_general[mes_pedido_letra][dia_pedido]["actividad"]))
            pass
        else:
            print("\nNo se encontró nada en esa fecha")
            mes_pedido = int(input("Escribe correctamente el mes que quieres verificar (expresa el mes en número): "))
            dia_pedido = int(input("Escribe correctamete el día de ese mes: "))

#opción 3
def eliminar_actividad(actividad_elim, mes_elim, dia_elim):
    while True:
        mes_elim = mes_escrito(mes_elim)
        if actividad_elim in biblioteca_general.get(mes_elim, {}).get(dia_elim, {}).get("actividad"):
            index_elim = biblioteca_general[mes_elim][dia_elim]["actividad"].index(actividad_elim)
            for x in biblioteca_general[mes_elim][dia_elim].keys():
                biblioteca_general[mes_elim][dia_elim][x].pop(index_elim)
            if biblioteca_general[mes_elim][dia_elim]["actividad"] == []:
                del biblioteca_general[mes_elim][dia_elim]
                if biblioteca_general[mes_elim] == {}:
                    del biblioteca_general[mes_elim]
            break
        else:
            print("\n No se encontró la actividad")
            actividad_elim = input("Escribe correctamente la actividad que queires eliminar: ")
            mes_pedido_letra = int(input("Escribe correctamente el mes de la actividad (expresa el mes en número): "))
            dia_pedido = int(input("Escribe correctamete el día de ese mes: "))

#main
año = int(input("¿en que año quieres agendar? " ))
while año <= 0:
    año = int(input("escribe un valor válido "))
dias_feb = bisciesto(año)

while True:
    accion = int(input("escribe 1 para agregar una actividad,\n2 para desplegar actividades de un dia,\n3 para eliminar una actividad o\n4 para terminar: "))
    print()
    if accion == 1:
        actividad, duracion, dia_inicio, mes_inicio_letra, hora_inicio, minuto_inicio, dia_final, mes_final_letra, hora_final, minuto_final = nuevo()
        print("\n",actividad, "dura", duracion, "minutos y es el", dia_inicio, "de", mes_inicio_letra, "a las", hora_inicio, ":", minuto_inicio, "y termina el", dia_final, "de", mes_final_letra, "a las", hora_final, ":", minuto_final, "\n")
    elif accion == 2:
        if biblioteca_general == {}:
            print("Aun no hay actividades\n")
        else:
            mes_pedido = int(input("¿Qué mes quieres revisar? (expresa el mes en número) "))
            dia_pedido = int(input("¿Qué día de ese mes? "))
            biblioteca_temp, longitud = recall(mes_pedido, dia_pedido)
            i = 0
            print()
            while i <= longitud-1:
                print(i+1, ". ", biblioteca_temp["actividad"][i], "dura", biblioteca_temp["duracion"][i], "minutos y es el", biblioteca_temp["dia_inicio"][i], "de", biblioteca_temp["mes_inicio_letra"][i], "a las", biblioteca_temp["hora_inicio"][i], ":", biblioteca_temp["minuto_inicio"][i], "y termina el", biblioteca_temp["dia_final"][i], "de", biblioteca_temp["mes_final_letra"][i], "a las", biblioteca_temp["hora_final"][i], ":", biblioteca_temp["minuto_final"][i])
                i = i + 1
            print()
            biblioteca_temp = {}
    elif accion == 3:
        if biblioteca_general == {}:
            print("Aun no hay actividades\n")
        else:
            actividad_elim = input("¿Qué actividad quieres eliminar? ")
            mes_elim = int(input("¿En que mes es esa actividad? "))
            dia_elim = int(input("¿En qué día de ese mes? "))
            eliminar_actividad(actividad_elim, mes_elim, dia_elim)
            print("\nActividad eliminada\n")
    elif accion == 4:
        break
    else:
        print("escribe un valor válido\n")
