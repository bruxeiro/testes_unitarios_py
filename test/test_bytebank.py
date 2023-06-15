from codigo.bytebank import Funcionario

class TestClass:


#Boa pratica: Fazer o teste o mais verboso possível
    def test_quando_idade_recebe_13_03_2000_deve_retornar_22(self):
        # Given - Contexto
        entrada = '13/03/2000'
        esperado = 23
        funcionario_teste = Funcionario('Teste', entrada, 1111)

        # When - Ação
        resultado = funcionario_teste.idade()

        # Then - Desfecho
        assert resultado ==esperado

    def test_quando_sobrenome_recebe_Lucas_Carvalho_deve_retornar_apenas_Carvalho(self):

        #ginven
        entrada = 'Lucas Carvalho'
        esperado = 'Carvalho'

        #When
        lucas = Funcionario(entrada, 1000, 11/11/2000)
        resultado = lucas.sobrenome()

        #Then
        assert resultado == esperado

    def test_quando_decrescimo_salario_recebe_100000_deve_retornar_90000(self):

        #ginven
        entrada = 100000
        entrada_nome = 'Paulo Bragança'
        esperado = 90000

        #When
        funcionario_teste = Funcionario(entrada_nome, '11/11/2000', entrada)
        funcionario_teste.decrescimo_salario()
        resultado = funcionario_teste.salario

        #Then
        assert resultado == esperado