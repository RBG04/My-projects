#entrada de dados
estacao=int(input("qual a estação do ano: "));
resultado=" "
#processamento
if(estacao==1):
    resultado="verao";
elif(estacao==2):
    resultado="inverno";
elif(estacao==3):
    resultado="outono";
elif(estacao==4):
    resultado="primavera";
#saida de dados
print(resultado);