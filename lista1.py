from typing import Union, Any

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import openpyxl
from matplotlib import colors
from matplotlib.ticker import PercentFormatter
from pandas import Series, DataFrame


def main():

    df = pd.read_excel("C:\\Users\\Administrador\\Documentos\\Meteorologia\\ClimatologiaII\\serie exercicios_lista1\\climato\\IAG_Cientec_Tmed_Precip diaria.xlsx",
                       sheet_name="IAG_temp_prec 2")


    df['Dia'] = pd.to_datetime(df['Dia'], format='%d/%m/%Y')

    #TODO: tirar caixinha do gráfico e ajustar eixo Y

    #Plot simples temperatura

    df.plot(x='Dia', y='TempMedia_oC', kind='line', color='red')
    plt.title("Série temporal da Temperatura média diária (°C)")
    plt.show()

    # Plot simples Precipitação
    df.plot(x='Dia', y='Precip_mm/d', kind='line')
    plt.title("Série temporal da Precipitação diária (mm/dia)")
    plt.show()


    # Hist frequência simples Temperatura
    temp = df['TempMedia_oC']
    plt.hist(temp, bins=5, weights=np.ones(len(temp)) / len(temp), color='red')
    plt.title("Histograma - Temperatura média diária (ºC)")
    plt.xlabel("Temperatura (°C)")
    pt.ylabel("Frequencia (%)")
    plt.gca().yaxis.set_major_formatter(PercentFormatter(1))
    plt.show()

    # Hist frequência acumulada Temperatura
    temp = df['TempMedia_oC']
    plt.hist(temp, bins=10, weights=np.ones(len(temp)) / len(temp), cumulative=True, color='red')
    plt.title("Histograma de frequência acumulada - Temperatura média diária (ºC)")
    plt.xlabel("Temperatura (°C)")
    pt.ylabel("Frequencia acumulada (%)")
    plt.gca().yaxis.set_major_formatter(PercentFormatter(1))
    plt.show()

    #TODO: variáveis com chuva e s/ chuva. Calcular as porcentagens de cada um
    x = df[df['Precip_mm/d']!=0]
    y = df[df['Precip_mm/d'] == 0]

    # Hist frequência simples Precipitação
    prec = x['Precip_mm/d']
    plt.hist(prec, bins=10, weights=np.ones(len(prec)) / len(prec))
    plt.title("Histograma - Precipitação diária (mm/d)")
    plt.xlabel("Precipitação (mm/dia)")
    pt.ylabel("Frequencia (%)")
    plt.gca().yaxis.set_major_formatter(PercentFormatter(1))
    plt.show()

    # Hist frequência acumulada Precipitação
    plt.hist(prec, bins=10, weights=np.ones(len(prec)) / len(prec), cumulative=True)
    plt.title("Histograma de frequência acumulada - Precipitação diária (mm/d)")
    plt.xlabel("Precipitação (mm/dia)")
    pt.ylabel("Frequencia acumulada (%)")
    plt.gca().yaxis.set_major_formatter(PercentFormatter(1))
    plt.show()

    # Histogram de frequência simples Ln(P)
    precln = np.log(prec)
    plt.hist(precln, bins=10, weights=np.ones(len(precln)) / len(precln))
    plt.tiitle ("Histograma de distribuição logarítmica - Precipitação diária (mm/dia)")
    plt.xlabel("Ln(P)")
    plt.ylabel("Frequência")
    plt.gca().yaxis.set_major_formatter(PercentFormatter(1))
    plt.show()

    # Histogram de frequência acumulada Ln(P)
    precln = np.log(prec)
    plt.hist(prec, bins=10, weights=np.ones(len(prec)) / len(prec), cumulative=True)
    plt.tiitle("Histograma de distribuição logarítmica - Precipitação diária (mm/dia)")
    plt.xlabel("Ln(P)")
    plt.ylabel("Frequência")
    plt.gca().yaxis.set_major_formatter(PercentFormatter(1))
    plt.show()

    #TODO: Plot de percentis (1%,50%,99%) dos histogramas de frequência acumulada.

    #TODO: Boxplots

    #TODO: verificar como rodar as estatísticas básicas pd.DataFrame.mean, ou df.mean? Não consegui rodar no console tbm

    #m = df.mean('TempMedia_oC', 'Precip_mm/d')  #pd. ou só a .mean ?
    #md = df.median("TempMedia_oC", "Precip_mm/d")
    #vr = df.var("TempMedia_oC", "Precip_mm/d")
    #st = df.std("TempMedia_oC", "Precip_mm/d")
    #sk = df.skw("TempMedia_oC", "Precip_mm/d")  # coeficiente de assimentria
    #rg = df.max("TempMedia_oC", "Precip_mm/d") - df.min("TempMedia_oC", "Precip_mm/d") #amplitude
    #cf_var = df.std("TempMedia_oC", "Precip_mm/d") / df.mean("TempMedia_oC",
                                                                 # "Precip_mm/d") * 100  # coeficiente de variação
    print(m, md, vr, st, sk, rg, cf_var)
main()