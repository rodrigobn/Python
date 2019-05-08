#19.	Faça um programa que peça o tamanho de um arquivo para download (em MB) 
# e a velocidade de um link de Internet (em MBps), calcule e informe o 
# tempo aproximado de download do arquivo usando este link (em minutos).

tamanhoArquivo = float(input("Tamanho do arquivo em MB: "))
velocidadeInternet = float(input("Velocidade da internet em MBps: "))

download = (tamanhoArquivo / velocidadeInternet) / 60

print("O download sera concluido em aproximadamente {:.2f} min".format(download))