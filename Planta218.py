import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
import os

planta218 = pd.read_excel(r'C:\Users\carlo\Desktop\desafio\data_plantas_python_1_1.xlsx', parse_dates= ["fecha_im"] )

planta31 = pd.read_excel(r'C:\Users\carlo\Desktop\desafio\data_plantas_python_2.xlsx',parse_dates= ["fecha_im"] )

total = pd.concat([planta218, planta31], axis=0)

"""Paso 1"""

planta218.plot.line(x='fecha_im', y='active_power_im')
plt.xlabel("Fecha")
plt.ylabel("Poder Activo")
plt.title("Datos Planta 218")
plt.savefig("Grafico planta 218.png")

"""Paso 2"""

"""Suma diaria active power"""
sums= planta218 ['active_power_im'].sum()

"""Max Active power"""
maxs= planta218 ['active_power_im'].max()


"""Min active power"""
mins= planta218 ['active_power_im'].min()


"""archivo txt"""
absFilepath =os.path.abspath(__file__)
path, filename =os.path.split(absFilepath)
grafico = open (path+"\Grafico planta 218.png")
s = sums
ma = maxs
mi = mins

graf=grafico
with open("Datos Planta 218.txt", "w") as text_file:
    text_file.write("La suma diaria de active power en esta planta es: %s\n" % s)
    text_file.write("El active power maximo en esta planta es: %s\n" % maxs)
    text_file.write("El active power minimo en esta planta es: %s\n" % mins)
    text_file.write("El grafico de esta planta se encuentra en: %s\n" % graf)
    text_file.close

"""paso 3"""
sumtotal= total['active_power_im'].sum()
print("La suma total de active power en ambas plantas es:",sumtotal)

