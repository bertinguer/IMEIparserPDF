# IMEIparserPDF

# Buscador de IMEI en PDF

Este script busca en un archivo PDF los números IMEI que se encuentren en el mismo.

## Requisitos
- Python 3
- PyPDF2

## Uso
`python3 pdf2imei.py fichero.pdf`

## Notas
- El script busca los IMEI en todas las páginas del archivo PDF
- El script busca IMEI con 14 o 15 digitos (en caso de tener 15 digitos se descartara el ultimo)
- El script busca los IMEI en las dos filas siguientes a la que contiene la palabra "IMEI" o "imei"

