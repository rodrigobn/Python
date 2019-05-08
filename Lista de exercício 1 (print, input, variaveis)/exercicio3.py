# c)	Faça um algoritmo que leia dois valores inteiros representando, 
# respectivamente, um valor de hora e um de minutos e informe quantos 
# minutos se passaram deste o início do dia. Exemplo: valores lidos: 13h 15min 
# impressão: 795 minutos

hora = int(input("Hora: "))
minuto = int(input("Minuto: "))

horaEmMinuto = hora * 60 + minuto

print(horaEmMinuto,"minutos")