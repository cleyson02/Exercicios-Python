qtdfuncionarios = 0
totalfilhos = 0

while True:
  qtdfilhos = int(input("Quantos filhos você tem? "))

  #condição de parada.
  if qtdfilhos < 0:
    break
    
  qtdfuncionarios += 1 #= qtdfuncionarios = qtdfuncionarios + 1
  totalfilhos += qtdfuncionarios
    
media = totalfilhos/qtdfuncionarios

print ("Média de filhos:", media)