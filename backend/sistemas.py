import pandas as pd
import numpy as np



def sistemaAmericano(monto,interes,plazo):

    columns = {"Numero de Cuota":[],"Monto Cuota":[],"Interes":[],"Amortizacion":[],"Monto Deuda":[]}
    montoCuota = interes*monto

    ultimaCuota = (interes *monto)+monto
    while plazo > 0:
        if plazo == 1:
            columns["Numero de Cuota"].append(plazo)
            columns["Interes"].append(montoCuota)
            columns["Monto Cuota"].append(ultimaCuota)
            columns["Amortizacion"].append(monto)
            columns["Monto Deuda"].append(0)
        else:
            columns["Numero de Cuota"].append(plazo)
            columns["Interes"].append(montoCuota)
            columns["Monto Cuota"].append(montoCuota)
            columns["Amortizacion"].append(0)
            columns["Monto Deuda"].append(monto)
        plazo -= 1

    columns["Numero de Cuota"]= columns["Numero de Cuota"][::-1]
    columns["Numero de Cuota"].append(0)
    columns["Monto Cuota"].append(0)
    columns["Interes"].append(sum(columns["Interes"]))
    columns["Amortizacion"].append(monto)
    columns["Monto Deuda"].append(0)


    df = pd.DataFrame(columns)
    df = df.set_index(df["Numero de Cuota"])
    df = df.drop(columns="Numero de Cuota")

    return df   






def sistemaAleman(v, n, i):
    k = 1
    ck = (v)/(n)+i*v
    totalInteres = 0
    totalAmortizacion = 0
    index = 1
    columns = {"Numero de Cuota":[],"Monto Cuota":[],"Interes":[],"Amortizacion":[],"Monto Deuda":[]}
    while(v > 0):
        columns["Monto Cuota"].append(ck)
        columns["Numero de Cuota"].append(index)
        ck = ck - i * (v/n)
        vk = v/n
        sk = (n - k + 1)*(v*i/n)
        columns["Interes"].append(sk)
        columns["Amortizacion"].append(vk)
        columns["Monto Deuda"].append(v)
        v = v - vk
        n = n - 1
        totalInteres = totalInteres + sk
        totalAmortizacion = totalAmortizacion + vk
       
        index += 1 
    columns["Numero de Cuota"].append(0)
    columns["Monto Cuota"].append(0)
    columns["Interes"].append(totalInteres)
    columns["Amortizacion"].append(totalAmortizacion)
    columns["Monto Deuda"].append(0)

    df = pd.DataFrame(columns)
    df = df.set_index(df["Numero de Cuota"])
    df = df.drop(columns="Numero de Cuota")

    return df






def sistemaFrances(v, n, i):
    k = 1
    c =  (v*i)/(1-(1+i)**-n)
    print(c)
    totalInteres = 0
    totalAmortizacion = v
    index = 1 
    columns = {"Numero de Cuota":[],"Monto Cuota":[],"Interes":[],"Amortizacion":[],"Monto Deuda":[]}
    while(v > 0):
        
        columns["Numero de Cuota"].append(index)
        sk = c*(1 - (1)/((1+i)**n+1-k))
        vk = (c)/((1+i)**n+1-k)
        ck = sk + vk
        columns["Monto Cuota"].append(ck)
        columns["Interes"].append(sk)
        columns["Amortizacion"].append(vk)
        columns["Monto Deuda"].append(v)
        v = v - vk
        n = n - 1
        totalInteres = totalInteres + sk
        #totalAmortizacion = totalAmortizacion + vk
        index +=1

    columns["Numero de Cuota"].append(0)
    columns["Monto Cuota"].append(0)
    columns["Interes"].append(totalInteres)
    columns["Monto Deuda"].append(0)
    columns["Amortizacion"].append(totalAmortizacion)

    df = pd.DataFrame(columns)
    df = df.set_index(df["Numero de Cuota"])
    df = df.drop(columns="Numero de Cuota")
    
    return df 

