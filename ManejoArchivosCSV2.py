import csv 

datos=[["pais","edad"],
["usa" , "entre 30 y 35"]]

with open("customers. csv","w",encoding="utf-8") as archivo:
    escribir=csv.writer(archivo)
    escribir.writerows(datos)