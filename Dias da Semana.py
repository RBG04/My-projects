#entrada de dados
semana=int(input("digite um numero de 1 a 7: "));

#processamento
if(semana==1):
    resultado="domingo";
elif(semana==2):
    resultado="segunda";
elif(semana==3):
    resultado="terça";
elif(semana==4):
    resultado="quarta";
elif(semana==5):
    resultado="quinta";
elif(semana==6):
    resultado="sexta";
elif(semana==7):
    resultado="sábado";
else:
    resultado="dia da semana inválido";
    
#saida de dados
print(resultado);