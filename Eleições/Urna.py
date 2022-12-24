import mysql.connector

banco = mysql.connector.connect(
    host="localhost",
    user="root",
    password="123456",
    database="urna"

)

#
class Candidato:
    def __init__(self, nome1,nome2):
        self.nome1 = nome1
        self.nome2 = nome2

    def anuncios(self):
        print(f"A eleição de 2022 conta com os seguintes candidatos: {self.nome1} do PL e {self.nome2} do PT.")


class Eleitores():
    def __init__(self, nome, idade, cpf, titulo, uf, endereco):
        self.nome = nome
        self.idade = idade
        self.cpf = cpf
        self.titulo = titulo
        self.uf = uf
        self.endereco = endereco

    def votar(self):
        while True:
            x = input("Olá Eleitor, deseja fazer algum cadastro? \n Digite 1 para Cadastrar \n Digite 2 para Sair \n")
            if x == "1":
                self.nome = input("digite seu nome ")
                self.idade = input("Digite sua idade ")
                self.cpf = input("Digite seu Cpf ")
                self.titulo = input("Digite o seu titulo ")
                self.uf = input("Digite seu UF ")
                self.endereco = input("Digite seu endereço ")
                break
                cursor = banco.cursor()
                sql = "INSERT INTO PESSOAS (nome,idade,cpf,uf,endereco) VALUES (%s,%s,%s,%s,%s,%s)"
                data = (self.nome,self.idade,self.cpf,self.uf,self.endereco)
                cursor.execute(sql,data)
                banco.commit()

            else:
                break

c1 = Candidato("Bolsonaro","Lula")
e1 = Eleitores("","","","","","")

c1.anuncios()
e1.votar()

