from os import system
from dataclasses import dataclass
from time import sleep
system("cls||clear")

dados = []

#Criando classe de dados:
@dataclass
class Pessoa:
    nome : str
    sobrenome : str
    idade : str
    peso : str
    altura : str
    sexo : str

#Função para criar arquivo txt:
def criando_arquivo(a,b):
    nome_do_arquivo = a
    lista_dados=b
    with open(nome_do_arquivo,"a") as arquivo_dados:
        for pessoa in lista_dados:
            arquivo_dados.write(f"{pessoa.nome},{pessoa.sobrenome},{pessoa.idade},{pessoa.peso},{pessoa.altura},{pessoa.sexo}\n")
    arquivo_dados.close()
    print("\n=== Dados Salvos ===\n")

#Função para ler arquivos criados:
def lendo_arquivo(a):
    nome_do_arquivo = a
    list_dados=[]
    with open(nome_do_arquivo,"r") as arquivo_origem:
        for linha in arquivo_origem:
            nome, sobrenome, idade, peso, altura, sexo = linha.strip().split(",")
            list_dados.append(Pessoa(nome=nome, sobrenome=sobrenome,idade=int(idade),peso=float(peso),altura=float(altura), sexo=sexo))
    arquivo_origem.close()
    return list_dados

#Função para calculo do IMC
def IMC (a,b,c):
        indice = c
        peso = a[indice]
        altura = b[indice]
        imc = peso/altura**2
        return imc

#Tabela saude:
def verificando_imc(imc):
    if imc < 18.5:
        print("Abaixo do peso")
    elif imc < 24.9:
        print("Peso normal")
    elif imc < 29.9:
        print("Sobrepeso")
    else:
        print("Obesidade")

#Menu inicial:
def menu ():
    print("="*60)
    print(f"{"CALCULADORA PARA O CORPO":^60}")
    print("="*60)
    print("-"*60)
    print("""
1- INSERIR DADOS
2- CALCULAR IMC 
3- TAXA METABÓLICA BASAL
4- PERCENTUAL DE GORDURA CORPORAL (ESTIMATIVA VIA IMC)
5- PESO IDEAL (FÓRMULA DE DIVINE)
6- ENCERRAR PROGRAMA
""")

#Taxa Metabolica:
def tax_metabolica(sexo,peso,idade,altura,posicao):
    i = posicao
    if sexo[i] == "MULHER":
        TMB_M = 447.6 + (9.2*peso[i])+(3.1*(altura[i]*100))-(4.3*idade[i])
        return TMB_M
    else:
        TMB_H=88.36 + (13.4*peso[i]) + (4.8*(altura[i]*100))-(5.7*idade[i])
        return TMB_H

#Percentual de Gordura:
def percentual_gordura (imc,idade,sexo,posicao):
    i = posicao
    if sexo[i] == "MULHER":
        percentual_mulheres = (1.20*imc)+(0.23*idade[i])-5.4
        return percentual_mulheres
    else:
        percentual_homens =(1.20*imc)+(0.23*idade[i])-16.2
        return percentual_homens

#Peso ideal:
def peso_ideal(altura,posicao,sexo):
    i = posicao
    if sexo[i] == "MULHER":
        peso_ideal_mulheres = 45.5+2.3*(((altura[i]*100)/2.54)-60)
        return peso_ideal_mulheres
    else:
        peso_ideal_homens =50+2.3*(((altura[i]*100)/2.54)-60)
        return peso_ideal_homens
        
while True:
    while True:
        system("cls||clear")
        menu()
        opcao = int(input(": "))
        if  opcao >= 1 and opcao <=6:
            break
    match (opcao):
        case 1:
            while True:
                print("="*42)
                print(f"{"INFORMAÇÔES":^42}")
                print("="*42)
                pessoa = Pessoa(
                    nome = input("\nNome: ").lower(),
                    sobrenome = input("sobrenome: "),
                    idade = int(input("Idade: ")),
                    peso = float(input("Peso: ")),
                    altura = float(input("Altura: ")),
                    sexo = input("Sexo: ").upper()
                )
                dados.append(pessoa)
                opcao = input("Desja adicionar outra pessoa ?").lower()
                if opcao == "não":
                    break
            nome_arquivo = "Dados para Exame.txt"
            criando_arquivo(nome_arquivo,dados)
            system("cls||clear")
        case 2:
            list_nome = []
            list_altura = []
            list_peso = []
            list_sobrenome = []
            dados = []
            system("cls||clear")
            print("="*42)
            print(f"{"CALCULANDO IMC":^42}")
            print("="*42)
            nome_arquivo = "Dados para Exame.txt"
            dados = lendo_arquivo(nome_arquivo)
            for dado in dados:
                list_nome.append(dado.nome)
                list_sobrenome.append(dado.sobrenome)
                list_altura.append(dado.altura)
                list_peso.append(dado.peso)
            while True:
                nome_seleção = input("Opção valida apenas para quem tenha adici-\nonados os dados anteriormente.\nInforme seu nome: ").lower()
                if nome_seleção in list_nome:
                    posicao = list_nome.index(nome_seleção)
                    break
                else:
                    print("Nome não encontrado, informe um \nnome cadastrado")
            nome_correto = list(map(str.capitalize, list_nome))
            imc=IMC(list_peso,list_altura,posicao)
            print("-"*42)
            print(f"Nome: {nome_correto[posicao]} {list_sobrenome[posicao]}")
            print(f"Altura: {list_altura[posicao]}")
            print(f"Peso: {list_peso[posicao]}")
            print(f"IMC: {imc:.2f}")
            verificando_imc(imc)
            print("-"*42)
            sleep(10)
        case 3:
            list_nome = []
            list_altura = []
            list_peso = []
            lista_idade = []
            list_sexo = []
            list_sobrenome =[]
            dados = []
            system("cls||clear")
            print("="*42)
            print(f"{"CALCULANDO TAXA METABÓLICA BASAL":^42}")
            print("="*42)
            nome_arquivo = "Dados para Exame.txt"
            dados = lendo_arquivo(nome_arquivo)
            for dado in dados:
                list_nome.append(dado.nome)
                list_sobrenome.append(dado.sobrenome)
                lista_idade.append(dado.idade)
                list_altura.append(dado.altura)
                list_peso.append(dado.peso)
                list_sexo.append(dado.sexo)
            while True:
                nome_seleção = input("Opção valida apenas para quem tenha adici-\nonados os dados anteriormente.\nInforme seu nome: ").lower()
                if nome_seleção in list_nome:
                    posicao = list_nome.index(nome_seleção)
                    break
                else:
                    print("Nome não encontrado, informe um \nnome cadastrado")
            nome_correto = list(map(str.capitalize, list_nome))
            taxa = tax_metabolica(list_sexo,list_peso,lista_idade,list_altura,posicao)
            print("-"*42)
            print(f"Nome: {nome_correto[posicao]} {list_sobrenome[posicao]}")
            print(f"Altura: {list_altura[posicao]}")
            print(f"Peso: {list_peso[posicao]}")
            print(f"Taxa Metabólica Basal (TMB): {taxa:.2f}")
            print("-"*42)
            sleep(10)
        case 4:
            list_nome = []
            list_altura = []
            list_peso = []
            list_sobrenome = []
            lista_sexo=[]
            lista_idade=[]
            dados = []
            system("cls||clear")
            print("="*42)
            print(f"{"CALCULANDO PERCENTUAL DE GORDURA":^42}")
            print("="*42)
            nome_arquivo = "Dados para Exame.txt"
            dados = lendo_arquivo(nome_arquivo)
            for dado in dados:
                list_nome.append(dado.nome)
                list_sobrenome.append(dado.sobrenome)
                list_altura.append(dado.altura)
                list_peso.append(dado.peso)
                lista_sexo.append(dado.sexo)
                lista_idade.append(dado.idade)
            while True:
                nome_seleção = input("Opção valida apenas para quem tenha adici-\nonados os dados anteriormente.\nInforme seu nome: ").lower()
                if nome_seleção in list_nome:
                    posicao = list_nome.index(nome_seleção)
                    break
                else:
                    print("Nome não encontrado, informe um \nnome cadastrado")
            nome_correto = list(map(str.capitalize, list_nome))
            imc=IMC(list_peso,list_altura,posicao)
            gordura = percentual_gordura(imc,lista_idade,lista_sexo,posicao)
            print("-"*42)
            print(f"Nome: {nome_correto[posicao]} {list_sobrenome[posicao]}")
            print(f"Altura: {list_altura[posicao]}")
            print(f"Peso: {list_peso[posicao]}")
            print(f"Percentual de gordura: {gordura:.2f} %")
            print("-"*42)
            sleep(10)
        case 5:
            list_nome = []
            list_altura = []
            lista_sexo = []
            list_sobrenome = []
            dados = []
            system("cls||clear")
            print("="*42)
            print(f"{"CALCULANDO PESO IDEAL":^42}")
            print("="*42)
            nome_arquivo = "Dados para Exame.txt"
            dados = lendo_arquivo(nome_arquivo)
            for dado in dados:
                list_nome.append(dado.nome)
                list_sobrenome.append(dado.sobrenome)
                list_altura.append(dado.altura)
                lista_sexo.append(dado.sexo)
            while True:
                nome_seleção = input("Opção valida apenas para quem tenha adici-\nonados os dados anteriormente.\nInforme seu nome: ").lower()
                if nome_seleção in list_nome:
                    posicao = list_nome.index(nome_seleção)
                    break
                else:
                    print("Nome não encontrado, informe um \nnome cadastrado")
            nome_correto = list(map(str.capitalize, list_nome))
            peso_id = peso_ideal(list_altura,posicao,lista_sexo)
            print("-"*42)
            print(f"Nome: {nome_correto[posicao]} {list_sobrenome[posicao]}")
            print(f"Altura: {list_altura[posicao]}")
            print(f"Peso ideal: {peso_id:.2f}")
            print("-"*42)
            sleep(10)
        case 6:
            break
