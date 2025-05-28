with open("himno.txt", "w", encoding="utf-8") as lector:
    contenido=lector.write("OH GLORIA\n")
print(contenido)

with open("himno.txt","a", encoding="utf-8") as archivo:
    sopa=archivo.write("inmarsesible\n")
print(sopa)

with open("himno.txt","r", encoding="utf-8") as archivo:
    sopa=archivo.readlines ()
print(sopa)

with open("himno.txt","r", encoding="utf-8") as archivo:
    sopa=archivo.readlines()
print(sopa[1])

