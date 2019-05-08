"""
19. Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são: 
  • "Telefonou para a vítima?" 
  • "Esteve no local do crime?" 
  • "Mora perto da vítima?" 
  • "Devia para a vítima?" 
  • "Já trabalhou com a vítima?" O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente". 
"""

contadorSim = 0
contadorNao = 0
perguntas = [
    "Telefonou para a vítima? (s)=sim, (n)=não ",
    "Esteve no local do crime? (s)=sim, (n)=não ",
    "Mora perto da vítima? (s)=sim, (n)=não ",
    "Devia para a vítima? (s)=sim, (n)=não ",
    "Já trabalhou com a vítima? (s)=sim, (n)=não "
]

for i in range(5):
    resposta = input(perguntas[i])
    while resposta != "s" and resposta != "n":
        print("Digite uma resposta valida! ")
        resposta = input()   
    if resposta == "s":
        contadorSim += 1
        resposta = ""
    else:
        contadorNao += 1
        resposta = ""

if contadorSim == 2:
    print("Suspeito")
elif 3 <= contadorSim <= 4:
    print("Cúmplice")
elif contadorSim == 5:
    print("Assassino")
else:
    print("Inocente")
