import re
import csv
import sys
import PyPDF2

def buscar_imeis(archivo):
    # Crear una lista vacía para almacenar los IMEI encontrados
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
                    if re.search(r'^\d{14,15}$',imei):
                        imei = imei[:14] if len(imei)==15 else imei
                        if imei not in imeis_encontrados:
                            imeis_encontrados.add(imei)
                            imei_valid = is_valid_imei(imei)
                            imeis_encontrados.add(imei_valid)
    return imeis_encontrados

def calculate_check_digit(imei):
    imei = str(imei)
    check_digit = 0
    for i, c in enumerate(imei):
        if i % 2 != 0:
            d = int(c) * 2
            if d > 9:
                d -= 9
            check_digit += d
        else:
            check_digit += int(c)
    check_digit = (10 - (check_digit % 10)) % 10
    return check_digit

def is_valid_imei(imei):
    imei = str(imei)[:14]
    check_digit = calculate_check_digit(imei)
    imei = imei + str(check_digit)
    return imei

def process_csv(output_file, imeis_encontrados):
    with open(output_file, 'w', newline='') as f_out:
        writer = csv.writer(f_out)
        headers = ['IMEI']
        writer.writerow(headers)
        for imei in imeis_encontrados:
            writer.writerow([imei])

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print('Uso: python script.py archivo.pdf output.csv')
        sys.exit(1)

    archivo = sys.argv[1]
    output_file = sys.argv[2]
