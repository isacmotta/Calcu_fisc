import numpy
from numpy import*
from tkinter import*
##-------------------------------------------#
print('Calculador...')
print('CRIADO POR ISAC MOTTA')
print('''
[!]Conversores
[1]Velocidade
[2]Medidas
''')
print("o programa e grande por isso esta partido em varios menus.")
sel=int(input('Selecionar a opção: '))
print('')
###
###
#Medidas
if sel ==2:
   print('Converter Medidas')
   



#Velocidade.
if sel==1:
   print('Envolvendo Velocidade')
   print('''
   [!]CONVERSORES
   --------------
   [1]km/s -> m/s
   [2]m/s -> km/s
   --------------
   [!]EQUAÇÕES  
   --------------
   [3]Torriceli
   [4]MRUV
   --------------
   ''')
   sel01=int(input('Selecione uma opção: '))
   #Conversores
   if sel01==1:
      #
      print('converter km/s -> m/s')
      #recolher dados
      km=float(input('Digite a velocidade em km/h: '))
      #calcular
      clc=km/3.16
      #levando o resultado
      while(clc>0):
         #quando o valor for acima de 0 esse valor sera exibido
         print('conversão concluida, de km/h {:.2f} para m/s deu {:.2f}m/s'.format(km,clc))
         print (" ")
      else:
         #se o valor for menor que 0 esse resultado sera exibido
         print('velocidade menor que 0 {:.2f}'.format(clc))
         print (" ")

   ###
   #Segunda conversão
   if sel01==2:
      print('de m/s para km/h')
      m=float(input('digite a velocidade em metro: '))
      clc01=m*3.16
      print('A conversão deu {:.3f}m/s'.format(clc01))
      print('finalizado')