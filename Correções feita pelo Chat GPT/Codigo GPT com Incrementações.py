import json
from os import system
from dataclasses import dataclass
from datetime import datetime
from time import sleep

# Criando classe para armazenar os dados históricos de cada pessoa
@dataclass
class DadosHistorico:
    data: str
    peso: float
    altura: float
    imc: float

    # Método para converter em dicionário
    def to_dict(self):
        return self.__dict__

# Classe Pessoa com histórico
@dataclass
class Pessoa:
    nome: str
    sobrenome: str
    idade: int
    sexo: str
    dados_historico: list

    # Método para converter em dicionário, incluindo histórico
    def to_dict(self):
        return {
            "nome": self.nome,
            "sobrenome": self.sobrenome,
            "idade": self.idade,
            "sexo": self.sexo,
            "dados_historico": [hist.to_dict() for hist in self.dados_historico]
        }

# Validação de entrada para garantir dados corretos
def entrada_validada(tipo, mensagem, min_valor=None, max_valor=None):
    while True:
        try:
            valor = tipo(input(mensagem))
            if min_valor is not None and valor < min_valor:
                print(f"Valor deve ser maior que {min_valor}.")
            elif max_valor is not None and valor > max_valor:
                print(f"Valor deve ser menor que {max_valor}.")
            else:
                return valor
        except ValueError:
            print("Entrada inválida, tente novamente.")

# Função para salvar dados em JSON
def salvar_dados_json(nome_arquivo, dados):
    with open(nome_arquivo, 'w') as f:
        json.dump([pessoa.to_dict() for pessoa in dados], f)

# Função para carregar dados de JSON
def ler_dados_json(nome_arquivo):
    try:
        with open(nome_arquivo, 'r') as f:
            dados = json.load(f)
        # Reconstruir instâncias de Pessoa e DadosHistorico
        return [Pessoa(
                    nome=p['nome'], 
                    sobrenome=p['sobrenome'], 
                    idade=p['idade'], 
                    sexo=p['sexo'], 
                    dados_historico=[DadosHistorico(**hist) for hist in p['dados_historico']]
                ) for p in dados]
    except FileNotFoundError:
        return []

# Função para cálculo de IMC
def calcular_imc(peso, altura):
    return peso / (altura ** 2)

# Função para verificar o status de saúde pelo IMC
def verificar_imc(imc):
    if imc < 18.5:
        return "Abaixo do peso"
    elif imc < 24.9:
        return "Peso normal"
    elif imc < 29.9:
        return "Sobrepeso"
    else:
        return "Obesidade"

# Função para gerar um relatório personalizado
def gerar_relatorio(nome, imc, peso_ideal):
    print(f"\nRelatório de Saúde para {nome}:")
    print(f"IMC: {imc:.2f}")
    print(f"Peso Ideal: {peso_ideal:.2f} kg")
    
    status = verificar_imc(imc)
    print(f"Status: {status}")
    
    if status == "Abaixo do peso":
        print("Recomendação: Aumente a ingestão calórica de forma saudável.")
    elif status == "Sobrepeso" or status == "Obesidade":
        print("Recomendação: Considere uma dieta balanceada e exercícios.")
    else:
        print("Recomendação: Mantenha um estilo de vida saudável.")

# Função para calcular peso ideal
def peso_ideal(altura, sexo):
    if sexo == "MULHER":
        return 45.5 + 2.3 * ((altura * 100 / 2.54) - 60)
    else:
        return 50 + 2.3 * ((altura * 100 / 2.54) - 60)

# Função para inserir novos dados de pessoa
def inserir_dados(dados):
    system("cls||clear")
    nome = input("Nome: ").lower()
    sobrenome = input("Sobrenome: ").lower()
    idade = entrada_validada(int, "Idade: ", 0, 120)
    sexo = input("Sexo (masculino/feminino): ").upper()
    peso = entrada_validada(float, "Peso (kg): ", 0)
    altura = entrada_validada(float, "Altura (m): ", 0, 3)
    data_atual = datetime.now().strftime("%Y-%m-%d")
    imc = calcular_imc(peso, altura)

    # Verificar se já existe uma pessoa com o mesmo nome
    for pessoa in dados:
        if pessoa.nome == nome and pessoa.sobrenome == sobrenome:
            pessoa.dados_historico.append(DadosHistorico(data=data_atual, peso=peso, altura=altura, imc=imc))
            print("Dados adicionados ao histórico da pessoa existente.")
            return

    nova_pessoa = Pessoa(
        nome=nome,
        sobrenome=sobrenome,
        idade=idade,
        sexo=sexo,
        dados_historico=[DadosHistorico(data=data_atual, peso=peso, altura=altura, imc=imc)]
    )
    dados.append(nova_pessoa)
    print("Pessoa adicionada com sucesso!")

# Função para visualizar histórico
def visualizar_historico(dados):
    nome_selecao = input("Informe seu nome: ").lower()
    sobrenome_selecao = input("Informe seu sobrenome: ").lower()

    for pessoa in dados:
        if pessoa.nome == nome_selecao and pessoa.sobrenome == sobrenome_selecao:
            print(f"Histórico de {pessoa.nome.capitalize()} {pessoa.sobrenome.capitalize()}:")
            for hist in pessoa.dados_historico:
                print(f"Data: {hist.data}, Peso: {hist.peso} kg, Altura: {hist.altura} m, IMC: {hist.imc:.2f}")
            return
    print("Pessoa não encontrada.")

# Função para calcular e mostrar o IMC e recomendações
def calcular_imc_e_relatorio(dados):
    nome_selecao = input("Informe seu nome: ").lower()
    sobrenome_selecao = input("Informe seu sobrenome: ").lower()

    for pessoa in dados:
        if pessoa.nome == nome_selecao and pessoa.sobrenome == sobrenome_selecao:
            ultimo_dado = pessoa.dados_historico[-1]
            imc = ultimo_dado.imc
            peso_id = peso_ideal(ultimo_dado.altura, pessoa.sexo)
            gerar_relatorio(pessoa.nome.capitalize(), imc, peso_id)
            return
    print("Pessoa não encontrada.")

# Menu inicial
def menu():
    print("=" * 60)
    print(f"{'CALCULADORA PARA O CORPO':^60}")
    print("=" * 60)
    print("""
1- INSERIR DADOS
2- VISUALIZAR HISTÓRICO
3- CALCULAR IMC E RELATÓRIO
4- ENCERRAR PROGRAMA
""")

# Loop principal
dados = ler_dados_json("dados_exame.json")

while True:
    system("cls||clear")
    menu()
    opcao = entrada_validada(int, ": ", 1, 4)

    if opcao == 1:
        inserir_dados(dados)
        salvar_dados_json("dados_exame.json", dados)
        sleep(2)
    elif opcao == 2:
        visualizar_historico(dados)
        sleep(5)
    elif opcao == 3:
        calcular_imc_e_relatorio(dados)
        sleep(5)
    elif opcao == 4:
        print("Encerrando o programa.")
        salvar_dados_json("dados_exame.json", dados)
        break
