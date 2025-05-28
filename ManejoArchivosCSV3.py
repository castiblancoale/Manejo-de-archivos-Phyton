import csv
datos=[["pais","edad"],
       ["usa","entre 30 y 35"]]

with open("empleados.csv", "a", encoding="utf-8") as archivo:
    filas=csv.writer(archivo)
    filas.writerows(datos)
