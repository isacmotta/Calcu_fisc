#inciando 
#importações de bibliotecas
import numpy
from numpy import*
from tkinter import*
print('Calculador físico:')
print('CRIADO POR ISAC MOTTA')
print('''
[1]Velocidade
[2]Distancia
[3]Tempo
[4]Calculador Atomico
[5]
[6]Peso
[7]Matematica 
[8]Universo(beta)
[9]
[10]
[x]sair
Use com
''')
sel=int(input('selecione uma opção: '))
#
#Calculos envolvendo velocidade
if sel==1:
    print('CÁLCULOS ENVOLVENDO VELOCIDADE')
    print('''
    [1]MRUV
    [2]Equação de Torriceli
    [3]
    ''')
    sel1=int(input(' '))

#VELOCIDADE_MRUV
    if sel1==1:
       print('MRUV')
       print('Vamos Começar')
       
#VELOCIDADE Torriceli
    elif sel1==2:
       print('Formula de Torriceli')

# 
#calculos envolvendo Distancias
elif sel==1:
   print('Calculos envolvendo distancia')
   print('''
   [1]Ano-Luz
   [2]Converso
   ''')
#
#tempo
if sel==3:
   print('tempo')
   print('''
   [1]Distorção Temporal a Partir da Velocidade 
   [2]
   [3]
   ''')
   sel2= int(input('Selecione a opção: '))
   #
   if sel2 ==1:
      print('Distorção temporal')

###
#universo
if sel==8:
   menu=Tk()
   menu.mainloop()