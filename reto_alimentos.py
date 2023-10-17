# reto_alimentos.py
#parcial 2 https://replit.com/join/qfnfnzyjps-diegok3
print("evaluaré tus alimentos y te diré si son  altos o bajos en azucar, sodio y grasa")
contenido_grasa = int(input("ingresa los gramos"
" de grasa por porción que tiene tu alimento"))
contenido_azucar = int(input("ahora ingresa los gramos de azucar por porción"))
contenido_sodio = int(input("por ultimo ingresa los mg de sodio que contiene"))

if contenido_grasa == contenido_grasa <= 5 and contenido_azucar <= 10:
  print("tu alimento es bajo en grasa y azucar")
  
elif contenido_sodio == contenido_sodio <= 100:
  print("tu alimento es bajo en sodio")

else:
  print("debes considerar las advertencias nutricionales")

#reto 2 porque me sobró tiempo
print("calcularé el riesgo de tu prestamo si ingresas los sig. datos")
cantidad_prestamo = int(input("ingresa la cantidad del prestamo"))
tasa_anual = int(input("ingresa el porcentaje de la tasa de interes anual"))
plazo = int(input("por ultimo ingresa el plazo al que pediste el prestamo en años"))

if tasa_anual == tasa_anual <= 5 and plazo <= 5:
  print("tu riesgo es bajo")
  
elif tasa_anual == tasa_anual > 5 or plazo > 5:
  print("tu riesgo es moderado")

else: 
  print("tu riesgo es alto")
