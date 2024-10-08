from os import system
from dataclasses import dataclass
from time import sleep

dados = []

#Criando classe de dados:
@dataclass
class Pessoa:
    nome : str
    sobrenome : str
    idade : str
    peso : str
    altura : str

#Função para criar arquivo txt:
def criando_arquivo(a,b):
    with open(a,"a") as arquivo_dados:
        for pessoa in b:
            arquivo_dados.write(f"{pessoa.nome},{pessoa.sobrenome},{pessoa.idade},{pessoa.peso},{pessoa.altura}\n")
    arquivo_dados.close()
    print("\n=== Dados Salvos ===\n")

#Função para ler arquivos criados:
def lendo_arquivo(a):
    list_dados=[]
    with open(a,"r") as arquivo_origem:
        for linha in arquivo_origem:
            nome, sobrenome, idade, peso, altura= linha.strip().split(",")
            list_dados.append(Pessoa(nome=nome, sobrenome=sobrenome, ))
    arquivo_origem.close()
    return list_dados


while True:
    system("cls||clear")
    pessoa = Pessoa(
        nome = input("Nome: "),
        sobrenome = input("sobrenome: "),
        idade = int(input("Idade: ")),
        peso = float(input("Peso: ")),
        altura = float(input("Altura: "))
    )
    dados.append(pessoa)
    
    opcao = input("Desja adicionar outra pessoa ?").lower()
    if opcao == "não":
        break
