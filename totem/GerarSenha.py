botao = ""
class senha:
    def __init__(self):
        pass


#Essa função deve buscar no banco de dados a ultima senha e com base nessa ultima senha gerar uma nova
    def calcularSenha(self):
        senhaAtual = 2
        senha = 1 + senhaAtual
        return senha


    def gerarsenha(self):
        if botao == "pressionado":
            self.calcularSenha()

        return senha


    