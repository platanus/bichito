archivo_notas = open("notas.txt", "r")
lineas_notas = archivo_notas.readlines()

suma_notas = 0
cuenta_notas = 0

for linea in lineas_notas:
  float_nota = float(linea)
  suma_notas += float_nota
  cuenta_notas += 1

promedio = suma_notas / cuenta_notas
print(promedio)

archivo_notas.close()
