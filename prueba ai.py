import csv

def suma_importes():
    # Abrir el archivo CSV
    nombre_archivo = input("ingrese el nombre")
    with open(nombre_archivo, "r") as f:
        reader = csv.reader(f)

        # Encontrar la columna "Imp. Total"
        headers = next(reader)
        col_index = headers.index("Imp. Total")
        tipo_fac = headers.index("Tipo")
        print(col_index)
        # Inicializar la variable total a 0
        total = 0

        # Leer cada fila del archivo y sumar el importe
        for row in reader:
            total += float(row[col_index])

    # Mostrar el total
    print(total)

suma_importes()