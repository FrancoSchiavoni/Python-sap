from datetime import datetime, timedelta

def generar_fechas(fecha_str):
    # Convertir la cadena de fecha a un objeto datetime
    fecha_inicio = datetime.strptime(fecha_str, "%d.%m.%Y")
    
    # Inicializar los arreglos
    fechas_lecturas = []
    fechas_calculo = []
    
    # Generar las 12 fechas para fechas_lecturas y fechas_calculo
    for i in range(12):
        # Calcular la fecha de lectura (último día del mes)
        ultimo_dia_mes = (fecha_inicio.replace(day=1) + timedelta(days=32)).replace(day=1) - timedelta(days=1)
        fechas_lecturas.append(ultimo_dia_mes.strftime("%d.%m.%Y"))
        
        # Calcular la fecha de cálculo (día 10 del mes siguiente)
        dia_10_mes_siguiente = (ultimo_dia_mes.replace(day=1) + timedelta(days=32)).replace(day=10)
        fechas_calculo.append(dia_10_mes_siguiente.strftime("%d.%m.%Y"))
        
        # Avanzar al mes siguiente para la próxima iteración
        fecha_inicio = (fecha_inicio.replace(day=1) + timedelta(days=32)).replace(day=1)
    
    return fechas_lecturas, fechas_calculo
