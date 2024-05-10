
import csv
import re
import pyperclip
from datetime import datetime

# def leerPortapapeles():
  #       lectura = pyperclip.paste()
    #     return lectura




def convertir_fecha(fecha):
    try:
        fecha = str.replace(fecha,"-","/")
        pattern = r'^\d{2}/\d{2}/\d{4}$'       # patron dd/mm/YYYY
        if re.match(pattern, fecha):
            return fecha
        # Intentamos analizar la fecha en formato "dd/mm/yy"
        fecha_obj = datetime.strptime(fecha, "%d/%m/%y")
        # Agregamos el siglo (20) al año para obtener "dd/mm/yyyy"
        fecha_completa = fecha_obj.strftime("%d/%m/%Y")  # patron dd/mm/YYYY
        return fecha_completa
    except ValueError:
       return "Error: "+fecha+" es Formato de fecha incorrecto. Debe ser dd/mm/yy."

# Supongamos que los datos están en un archivo CSV llamado 'tabla.csv'
# Cambia esto según tu caso real

# Diccionario para almacenar los datos
datos_por_columna = {}



# try:
    # contenidoPortapapeles = leerPortapapeles()
    # print(contenidoPortapapeles)
    # archivo_csv = 'c:/Users/USER/OneDrive/Documentos/python/De_Excel_A_Damdata/tablaTEST.csv'
    # with open(archivo_csv,"w") as archive:
        # archive.write(contenidoPortapapeles)
# except ValueError:
archivo_csv = 'c:/Users/USER/OneDrive/Documentos/python/De_Excel_A_Damdata/tabla.csv'

# Leer el archivo CSV
with   open(archivo_csv, 'r') as archivo:
    lector_csv = csv.reader(archivo, delimiter='\t')
    encabezados = next(lector_csv)  # La primera fila contiene los nombres de columna

    # Inicializar el diccionario con listas vacías para cada columna
    for columna in encabezados[1:]:
        datos_por_columna[columna] = []

    # Procesar las filas restantes
    for fila in lector_csv:
        TXTfecha = str(fila[0])  # NO LA CONVIERTO Convertir la fecha a objeto datetime

        # Asociar los valores numéricos con los nombres de columna
        for i, columna in enumerate(encabezados[1:]):
            valor = str.replace(str.replace(fila[i + 1]," ",""),".",",")  # Suponemos que los valores son números
            datos_por_columna[columna].append(( TXTfecha, valor))

contenido=""
# Imprimir los resultados
for columna, datos in datos_por_columna.items():
    #  print(f"Columna '{columna}':")
    for fecha, valor in datos:
       if columna:
            print(convertir_fecha(fecha)+" 08:00:00;"+ columna+";"+valor)
            contenido += convertir_fecha(fecha)+" 08:00:00;"+ columna+";"+valor +";;;;\n"


salida_csv="c:/Users/USER/OneDrive/Documentos/python/De_Excel_A_Damdata/tablaSALIDA.csv"
print("Guardado es:.......\n"+contenido)
with open(salida_csv,"w") as file:
    file.write(contenido)

print("***************")
print("* Guardado en *")
print(" en: "+ salida_csv)
print("***************")