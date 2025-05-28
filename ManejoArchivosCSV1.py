import csv
# with open("customers.csv", "r", encoding="utf-8") as archivo:
#     contenido=csv.reader(archivo)
#     for x in contenido:
#         print(x)

# with open("customers.csv","r", encoding="utf-8") as archivo:
#     filas=csv.DictReader(archivo)
#     for x in filas:
#         print(x["First Name"], x["Company"])

datos=[["pais","edad"],
["usa" , "entre 30 y 35"]]

with open("customers. csv","w",encoding="utf-8") as archivo:
    escribir=csv.writer(archivo)
    escribir.writerows(datos)

