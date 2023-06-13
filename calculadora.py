#inciando 
#importações de bibliotecas
import numpy
from numpy import*
print('Calculador físico:')
print('CRIADO POR ISAC MOTTA')
print('''
[1]Velocidade
[2]Distancia
[3]Tempo
[4]Calculador Atomico
[5]
[6]

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
       print('')
#VELOCIDADE Torriceli
    elif sel1==2:
       print('')
#calculos envolvendo Distancias
elif sel==1:
   print('Calculos envolvendo distancia')
   print('''
   [1]Ano-Luz
   [2]Converso
   ''')
#tempo
if sel==3:
   print('tempo')
   print('''
   [1]Numero Atomico 
   [2]
   [3]
   ''')