'''
#entrada de dados
idade=int(input("digite sua idade: "))
resultado=''

#processamento
if (idade>=1 and idade <=11):
    resultado="Criança"
elif(idade>11 and idade<=18):
    resultado="Adolecente"
elif(idade>18 and idade<=39):
    resultado="Jovem"
elif(idade>=40 and idade<=59):
    resultado="Adulto"
else:
    resultado="Idoso"

#saida de dados
print(resultado)
'''