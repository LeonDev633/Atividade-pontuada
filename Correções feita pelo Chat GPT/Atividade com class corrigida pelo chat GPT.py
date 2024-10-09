from os import system
from dataclasses import dataclass
from time import sleep

dados = []

# Criando classe de dados:
@dataclass
class Pessoa:
    nome: str
    sobrenome: str
    idade: int
    peso: float
    altura: float
    sexo: str

# Função para criar arquivo txt:
def criando_arquivo(a, b):
    nome_do_arquivo = a
    lista_dados = b
    with open(nome_do_arquivo, "a") as arquivo_dados:
        for pessoa in lista_dados:
            arquivo_dados.write(f"{pessoa.nome},{pessoa.sobrenome},{pessoa.idade},{pessoa.peso},{pessoa.altura},{pessoa.sexo}\n")
    print("\n=== Dados Salvos ===\n")

# Função para ler arquivos criados:
def lendo_arquivo(a):
    nome_do_arquivo = a
    list_dados = []
    with open(nome_do_arquivo, "r") as arquivo_origem:
        for linha in arquivo_origem:
            nome, sobrenome, idade, peso, altura, sexo = linha.strip().split(",")
            list_dados.append(Pessoa(nome=nome, sobrenome=sobrenome, idade=int(idade), peso=float(peso), altura=float(altura), sexo=sexo))
    return list_dados

# Função para calculo do IMC
def IMC(a, b, c):
    indice = c
    peso = a[indice]
    altura = b[indice]
    imc = peso / altura**2
    return imc

# Tabela de saúde:
def verificando_imc(imc):
    if imc < 18.5:
        print("Abaixo do peso")
    elif imc < 24.9:
        print("Peso normal")
    elif imc < 29.9:
        print("Sobrepeso")
    else:
        print("Obesidade")

# Menu inicial:
def menu():
    print("="*60)
    print(f"{'CALCULADORA PARA O CORPO':^60}")
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

# Taxa Metabólica Basal:
def tax_metabolica(sexo, peso, idade, altura, posicao):
    i = posicao
    if sexo[i] == "MULHER" or sexo[i] == "FEMININO":
        TMB_M = 447.6 + (9.2 * peso[i]) + (3.1 * (altura[i] * 100)) - (4.3 * idade[i])
        return TMB_M
    else:
        TMB_H = 88.36 + (13.4 * peso[i]) + (4.8 * (altura[i] * 100)) - (5.7 * idade[i])
        return TMB_H

# Percentual de Gordura:
def percentual_gordura(imc, idade, sexo, posicao):
    i = posicao
    if sexo[i] == "MULHER" or sexo[i] == "FEMININO":
        percentual_mulheres = (1.20 * imc) + (0.23 * idade[i]) - 5.4
        return percentual_mulheres
    else:
        percentual_homens = (1.20 * imc) + (0.23 * idade[i]) - 16.2
        return percentual_homens

# Peso ideal:
def peso_ideal(altura, posicao, sexo):
    i = posicao
    if sexo[i] == "MULHER" or sexo[i] == "FEMININO":
        peso_ideal_mulheres = 45.5 + 2.3 * (((altura[i] * 100) / 2.54) - 60)
        return peso_ideal_mulheres
    else:
        peso_ideal_homens = 50 + 2.3 * (((altura[i] * 100) / 2.54) - 60)
        return peso_ideal_homens

# Função principal
while True:
    while True:
        system("cls||clear")
        menu()
        try:
            opcao = int(input(": "))
            if 1 <= opcao <= 6:
                break
        except ValueError:
            print("Por favor, insira uma opção válida!")

    if opcao == 6:
        print("Encerrando o programa...")
        break

    match opcao:
        case 1:
            while True:
                try:
                    print("="*42)
                    print(f"{'INFORMAÇÕES':^42}")
                    print("="*42)
                    pessoa = Pessoa(
                        nome=input("\nNome: ").lower(),
                        sobrenome=input("Sobrenome: "),
                        idade=int(input("Idade: ")),
                        peso=float(input("Peso (kg): ")),
                        altura=float(input("Altura (m): ")),
                        sexo=input("Sexo (masculino/feminino): ").upper()
                    )
                    dados.append(pessoa)
                except ValueError:
                    print("Erro na entrada de dados. Verifique se os campos estão corretos.")
                    continue

                opcao = input("Deseja adicionar outra pessoa? (sim/não): ").lower()
                if opcao == "não":
                    break
            nome_arquivo = "Dados_para_Exame.txt"
            criando_arquivo(nome_arquivo, dados)
            system("cls||clear")

        case 2:
            if not dados:
                nome_arquivo = "Dados_para_Exame.txt"
                dados = lendo_arquivo(nome_arquivo)

            list_nome = [p.nome for p in dados]
            list_altura = [p.altura for p in dados]
            list_peso = [p.peso for p in dados]
            list_sobrenome = [p.sobrenome for p in dados]

            while True:
                nome_selecao = input("Informe seu nome: ").lower()
                if nome_selecao in list_nome:
                    posicao = list_nome.index(nome_selecao)
                    break
                else:
                    print("Nome não encontrado. Informe um nome cadastrado.")

            nome_correto = list(map(str.capitalize, list_nome))
            imc = IMC(list_peso, list_altura, posicao)
            print("-"*42)
            print(f"Nome: {nome_correto[posicao]} {list_sobrenome[posicao]}")
            print(f"Altura: {list_altura[posicao]} m")
            print(f"Peso: {list_peso[posicao]} kg")
            print(f"IMC: {imc:.2f}")
            verificando_imc(imc)
            print("-"*42)
            sleep(10)

        case 3:
            if not dados:
                nome_arquivo = "Dados_para_Exame.txt"
                dados = lendo_arquivo(nome_arquivo)

            list_nome = [p.nome for p in dados]
            list_altura = [p.altura for p in dados]
            list_peso = [p.peso for p in dados]
            lista_idade = [p.idade for p in dados]
            list_sexo = [p.sexo for p in dados]
            list_sobrenome = [p.sobrenome for p in dados]

            while True:
                nome_selecao = input("Informe seu nome: ").lower()
                if nome_selecao in list_nome:
                    posicao = list_nome.index(nome_selecao)
                    break
                else:
                    print("Nome não encontrado. Informe um nome cadastrado.")

            nome_correto = list(map(str.capitalize, list_nome))
            taxa = tax_metabolica(list_sexo, list_peso, lista_idade, list_altura, posicao)
            print("-"*42)
            print(f"Nome: {nome_correto[posicao]} {list_sobrenome[posicao]}")
            print(f"Altura: {list_altura[posicao]} m")
            print(f"Peso: {list_peso[posicao]} kg")
            print(f"Taxa Metabólica Basal (TMB): {taxa:.2f} kcal/dia")
            print("-"*42)
            sleep(10)

        case 4:
            if not dados:
                nome_arquivo = "Dados_para_Exame.txt"
                dados = lendo_arquivo(nome_arquivo)

            list_nome = [p.nome for p in dados]
            lista_idade = [p.idade for p in dados]
            list_sexo = [p.sexo for p in dados]
            list_sobrenome = [p.sobrenome for p in dados]

            while True:
                nome_selecao = input("Informe seu nome: ").lower()
                if nome_selecao in list_nome:
                    posicao = list_nome.index(nome_selecao)
                    break
                else:
                    print("Nome não encontrado. Informe um nome cadastrado.")

            nome_correto = list(map(str.capitalize, list_nome))
            imc = IMC([p.peso for p in dados], [p.altura for p in dados], posicao)
            gordura = percentual_gordura(imc, lista_idade, list_sexo, posicao)
            print("-"*42)
            print(f"Nome: {nome_correto[posicao]} {list_sobrenome[posicao]}")
            print(f"IMC: {imc:.2f}")
            print(f"Percentual estimado de gordura: {gordura:.2f}%")
            print("-"*42)
            sleep(10)

        case 5:
            if not dados:
                nome_arquivo = "Dados_para_Exame.txt"
                dados = lendo_arquivo(nome_arquivo)

            list_nome = [p.nome for p in dados]
            list_altura = [p.altura for p in dados]
            list_sexo = [p.sexo for p in dados]
            list_sobrenome = [p.sobrenome for p in dados]

            while True:
                nome_selecao = input("Informe seu nome: ").lower()
                if nome_selecao in list_nome:
                    posicao = list_nome.index(nome_selecao)
                    break
                else:
                    print("Nome não encontrado. Informe um nome cadastrado.")

            nome_correto = list(map(str.capitalize, list_nome))
            peso = peso_ideal(list_altura, posicao, list_sexo)
            print("-"*42)
            print(f"Nome: {nome_correto[posicao]} {list_sobrenome[posicao]}")
            print(f"Altura: {list_altura[posicao]} m")
            print(f"Peso ideal: {peso:.2f} kg")
            print("-"*42)
            sleep(10)
