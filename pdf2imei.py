import re
import sys
import PyPDF2

def buscar_imeis(archivo):
    # Crear un set vacío para almacenar los IMEI encontrados
    imeis_encontrados = set()

    # Abrimos el archivo PDF
    with open(archivo, 'rb') as archivo:
        lector = PyPDF2.PdfReader(archivo)

        # Leemos todas las páginas del PDF
        for i in range(len(lector.pages)):
            pagina = lector.pages[i]
            texto = pagina.extract_text()
            lineas = texto.split('\n')
            imei = ''
            for j, linea in enumerate(lineas):
                # Buscamos el IMEI en el texto de la página
                if re.search(r'(?:IMEI|imei)',linea, re.IGNORECASE):
                    imei = lineas[j+1]
                    if re.search(r'^\d{14}|\d{15}|\d{16}$',imei):
                        if imei not in imeis_encontrados:
                            imeis_encontrados.add(imei)

    # Imprimimos los IMEIs encontrados
    for imei in imeis_encontrados:
        print(f'{imei}')

"""
        for i in range(len(lector.pages)):
            pagina = lector.pages[i]
            texto = pagina.extract_text()
            lineas = texto.split('\n')
            imei = ''
            for j, linea in enumerate(lineas):
                # Buscamos el IMEI en el texto de la página
                if re.search(r'(?:IMEI|imei)',linea, re.IGNORECASE):
                    imei = lineas[j+1]
                    if re.search(r'^\d{14}|\d{15}|\d{16}$',imei):
                        #imei = imei[:14] if len(imei)>=14 else imei
                        #if imei not in imeis_encontrados:
                            #imeis_encontrados.add(imei)
                            print(f'{imei}')
"""

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Uso: python script.py archivo.pdf')
        sys.exit(1)

    archivo = sys.argv[1]
    buscar_imeis(archivo)
