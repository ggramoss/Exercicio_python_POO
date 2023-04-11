#
# Tarefa 1
# Competências avaliadas:
# - Saber interpretar o que foi solicitado
# - Desenvolver uma solução viável para o problema
# - Saber utilizar classes e objetos

'''
Faça um algoritmo que controle o acesso de pessoas a
um estabelecimento comercial.

Para isso você deverá utilizar as seguintes classes:

Crie uma classe Profissional com os atributos:
        - nome
        - especialidade
        - sala
    Todos atributos devem ser privados e string.

crie uma classe Visitante com os atributos:
        - nome
        - documento
    Todos atributos devem ser privados e string.

crie a classe Visita com os atributos:
        - visitante
        - profissional
        - data_visita
    O atributo visitante deverá ser um objeto da
        classe Visitante escolhido de lista_visitantes.
    O atributo profissional deverá ser um objeto da
        classe Profissional escolhido de lista_profissionais.

Crie os métodos que forem necessários para acessar os
atributos das classes.


Desenvolva seu código a partir do menu abaixo:

======================
MENU
======================
1- Cadastrar Profissional
2- Localizar Profissional
3- Cadastrar Visitante
4- Registrar Visita
5- Relatório de Conferência
Escolha:


Na opção 1 do menu cadastre o nome, especialidade e sala
    onde o profissional atende. Armazene esses dados em
    lista_Profissionais (como objetos).

Na opção 2 do menu é possível localizar um profissional
    pelo nome ou pela profissão. Isso serve para o caso
    do visitante não saber a sala do profissional.
    (Apenas mostrar na tela o nome e a sala do profissional)

Na opção 3 do menu será cadastrado o visitante com nome,
    documento. Armazene esses dados em lista_visitantes
    (como objetos).

Na opção 4 do menu será registrado a visita.
    Escolha o visitante (da lista de visitantes) e o
    profissional (da lista_profissionais), entre com a
    data e armazene a visita em lista_visitas
    (como objeto).

Na opção 5 do menu apenas crie um relatório de conferência.
    Selecione o Profissional e mostre todos os visitantes
    e a data da visita.

Obs. Em todas as listas serão armazenados as instâncias
de suas classes.

'''


# Classes:

class Profissional:
    def __init__(self, nome, especialidade, sala):
        self.__nome = nome
        self.__especialidade = especialidade
        self.__sala = sala

    def get_nome(self):
        return self.__nome

    def get_especialidades(self):
        return self.__especialidade

    def get_sala(self):
        return self.__sala


class Visitante:
    def __init__(self, nome, documento):
        self.__nome = nome
        self.__documento = documento

    def get_nome(self):
        return self.__nome

    def get_documento(self):
        return self.__documento


class Visita:
    def __init__(self, visitante, profissional, data):
        self.__visitante = visitante
        self.__profissional = profissional
        self.__data = data

    def get_visitante(self):
        return f"{self.__visitante}"

    def get_profissional(self):
        return self.__profissional

    def get_data(self):
        return self.__data


# Listas e Funções:

lista_profissional = []
lista_visitante = []
lista_visita = []


def cadastrar_profissional():
    nome = input("Digite o nome do profissional: ")
    especialidade = input("Digite a especialidade do profissional: ")
    sala = input("Digite a sala do profissional: ")
    objprofissional = Profissional(nome, especialidade, sala)
    lista_profissional.append(objprofissional)
    print("Profissional cadastrado com sucesso!!")


def localizar_profissional():
    nome = input("Digite o nome do profissional:")
    for profissional in lista_profissional:
        if profissional.get_nome() == nome:
            print(f"Profissional: {profissional.get_nome()}")
            print(f"Sala: {profissional.get_sala()}")
        else:
            print("Profissional não cadastrado")


def cadastrar_visitante():
    nome = input("Digite o nome do visitante:")
    documento = input("Digite o documento do visitante:")
    objvisitante = Visitante(nome, documento)
    lista_visitante.append(objvisitante)
    print("Visitante cadastrado com sucesso!!")


def registra_visita():
    nome_visita = input("Digite o nome do visitante: ")
    for visitante in lista_visitante:
        if visitante.get_nome() == nome_visita:
            nome_profissional = input("Digite o nome do profissional que vai ser visitado:")
            for profissional in lista_profissional:
                if profissional.get_nome() == nome_profissional:
                    data = input("Digite a data da visita:")
                    visita = Visita(nome_visita, nome_profissional, data)
                    lista_visita.append(visita)
                    print("Visita cadastrada com sucesso!!")

                else:
                    print("Profissional não encontrado")
        else:
            print("Visitante não encontrado")



def relatorio():
    for visita in lista_visita:
        print(f"Visitante:{visita.get_visitante()}-----Profissional:{visita.get_profissional()}-----Data:{visita.get_data()}")


def menu():

        while True:
            escolha = input(
            '''
            ==========================
            -----------MENU-----------
            ==========================
            1- Cadastrar Profissional
            2- Localizar Profissional
            3- Cadastrar Visitante
            4- Registrar Visita
            5- Relatório de Conferência
            Escolha:''')


            if escolha == "1":
                cadastrar_profissional()

            if escolha == "2":
                localizar_profissional()

            if escolha == "3":
                cadastrar_visitante()

            if escolha == "4":
                registra_visita()

            if escolha == "5":
                print("---------------------------------------RELATÓRIO----------------------------------------")
                relatorio()

            if escolha > "5":
                print("Ops! Digite um numero existente no menu")



menu()
