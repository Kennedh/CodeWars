"""
Softwares de reconhecimento de caracteres são amplamente utilizados para digitalizar textos impressos. Assim, os textos
podem ser editados, pesquisados e armazenados em um computador.

Quando documentos (especialmente aqueles bem antigos, escritos em máquina de escrever) são digitalizados, softwares de
reconhecimento de caracteres frequentemente cometem erros.

Sua tarefa é corrigir os erros no texto digitalizado. Você só precisa corrigir os seguintes erros:

S é mal interpretado como 5
O é mal interpretado como0
I é mal interpretado como1
Os casos de teste contêm números apenas por engano.

"""

def correct(s):
    return s.replace("5","S").replace("0","O").replace("1","I")

# Teste

print(correct("L0ND0N"))
print(correct("DUBL1N"))
print(correct("51NGAP0RE"))
print(correct("BUDAPE5T"))
print(correct("PAR15"))
