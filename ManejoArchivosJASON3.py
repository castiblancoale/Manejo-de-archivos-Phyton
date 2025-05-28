import json
datos=[{"pais":"rusa",},{"talento" :"ventas"}]

with open("people. json","a") as archivo:
    dicci=json.dump(datos,archivo, indent=4)