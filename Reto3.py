def simulador_prestamo_yo_le_fio(datos_venta:dict)->dict:
    datos_credito = {
        "saldo financiar" : datos_venta["venta"]- datos_venta["cuota inicial"],
    }
    amortizacion = list()


    TMV = pow(1+(datos_venta["interes anual"]/100),1/12) - 1 

    saldo_a_financiar = round(datos_venta["venta"] - datos_venta["cuota inicial"],0)
    cuota = round(saldo_a_financiar/ ((1-pow(1+TMV, -datos_venta["cuotas"]))/TMV),0)

    datos_credito["cuota"] = cuota

    saldo = saldo_a_financiar

    for n_cuota in range(int(datos_venta["cuotas"])):
        
        valor_interes = round(saldo * TMV, 2)
        capital = round(cuota - valor_interes, 2)

        if n_cuota == datos_venta["cuotas"]-1:
            cuota = round(saldo + valor_interes,2)
            capital = round(saldo, 2)
            
        saldo =  round(saldo-capital,2)
        amortizacion.append((n_cuota+1,capital,valor_interes,cuota,saldo))
    
    datos_credito["amortizacion"] = amortizacion
    return datos_credito
        
datos_venta = { "venta": 2000000.0, "cuota inicial": 0.0, "cuotas": 6, "interes anual": 28.99 }

print(simulador_prestamo_yo_le_fio(datos_venta))




#{ "venta": 2000000.0, "cuota inicial": 0.0, "cuotas": 6, "interes anual": 28.99 }
