archivo_notas = open("notas.txt", "r")

primera_nota = float(archivo_notas.readline())
segunda_nota = float(archivo_notas.readline())
tercera_nota = float(archivo_notas.readline())
cuarta_nota = float(archivo_notas.readline())

promedio = sum([primera_nota, segunda_nota, tercera_nota, cuarta_nota]) / 4
print(promedio)

archivo_notas.close()
