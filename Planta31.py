import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

planta218 = pd.read_excel(r'C:\Users\carlo\Desktop\desafio\data_plantas_python_1_1.xlsx', parse_dates= ["fecha_im"] )

planta31 = pd.read_excel(r'C:\Users\carlo\Desktop\desafio\data_plantas_python_2.xlsx',parse_dates= ["fecha_im"] )

total = pd.concat([planta218, planta31], axis=0)

"""Paso 1"""

planta31.plot.line(x='fecha_im', y='active_power_im')
plt.xlabel("Fecha")
plt.ylabel("Poder Activo")
plt.title("Datos Planta 31")
plt.savefig("c:/Users/carlo/Desktop/desafio/Grafico planta 31.png")


"""Paso 2"""

"""Suma diaria active power"""
sums= planta31 ['active_power_im'].sum()

"""Max Active power"""
maxs= planta31 ['active_power_im'].max()


"""Min active power"""
mins= planta31 ['active_power_im'].min()


"""archivo txt"""
s = sums
ma = maxs
mi = mins
with open("Datos Planta 31.txt", "w") as text_file:
    text_file.write("La suma diaria de active power en esta planta es: %s\n" % s)
    text_file.write("El active power maximo en esta planta es: %s\n" % maxs)
    text_file.write("El active power minimo en esta planta es: %s\n" % mins)
    
"""paso 3"""
sumtotal= total['active_power_im'].sum()
print("La suma total de active power en ambas plantas es:",sumtotal)