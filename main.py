from bytebank import Funcionario

#lucas = Funcionario('Lucas Caravalho', '13/03/2000', 1000)

#print(lucas.idade())

def teste_idade():
    funcionario_teste = Funcionario('Teste', '13/03/2000', 11111)
    print(f'Teste = {funcionario_teste.idade()}')


teste_idade()