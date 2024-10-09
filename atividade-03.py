import os



# Função sem retorno.
def logoSenai():
    os.system("cls || clear")
    print("="*20)
    print("="*5,f"{"SENAI":^8}","="*5)
    print("="*20)

def nivel_obesidade (a,b,c,d,e,f):
    for i,imc in enumerate(a):
        if imc < 18.5:
            print("="*20)
            print(f"{"ABAIXO DO PESO":^20}")
            print(f"NOME: {b[i]} {d[i]} ")
            print(f"IDADE: {c[i]}")
            print(f"SEU IMC É {imc:.2f}")
            print(f"ALTURA: {e[i]}")
            print(f"PESO: {f[i]}")
            print("="*20)
        elif imc >= 18.5 and imc < 25:
            print("="*20)
            print(f"{"PESO NORMAL":^20}")
            print(f"NOME: {b[i]} {d[i]} ")
            print(f"IDADE: {c[i]}")
            print(f"SEU IMC É {imc:.2f}")
            print(f"ALTURA: {e[i]}")
            print(f"PESO: {f[i]}")
            print("="*20)
        elif imc >= 25 and imc < 30:
            print("="*20)
            print(f"{"SOBREPESO":^20}")
            print(f"NOME: {b[i]} {d[i]} ")
            print(f"IDADE: {c[i]}")
            print(f"SEU IMC É {imc:.2f}")
            print(f"ALTURA: {e[i]}")
            print(f"PESO: {f[i]}")
            print("="*20)
        elif 30 <= imc <35:
            print("="*20)
            print(f"{"OBESIDADE GRAU I":^20}")
            print(f"NOME: {b[i]} {d[i]} ")
            print(f"IDADE: {c[i]}")
            print(f"SEU IMC É {imc:.2f}")
            print(f"ALTURA: {e[i]}")
            print(f"PESO: {f[i]}")
            print("="*20)
        elif 30 <= imc <35:
            print("="*20)
            print(f"{"OBESIDADE GRAU II":^20}")
            print(f"NOME: {b[i]} {d[i]} ")
            print(f"IDADE: {c[i]}")
            print(f"SEU IMC É {imc:.2f}")
            print(f"ALTURA: {e[i]}")
            print(f"PESO: {f[i]}")
            print("="*20)
        elif 30 <= imc <35:
            print("="*20)
            print(f"{"OBESIDADE GRAU III (MO)":^20}")
            print(f"NOME: {b[i]} {d[i]} ")
            print(f"IDADE: {c[i]}")
            print(f"SEU IMC É {imc:.2f}")
            print(f"ALTURA: {e[i]}")
            print(f"PESO: {f[i]}")
            print("="*20)

def IMC (a:float, b:float):
    lista_imcs = []
    for i,peso in enumerate(b):
        imc = peso/(a[i]*a[i])
        lista_imcs.append(imc)
    return lista_imcs
# Definindo listas vazias para armazenar os dados dos usuários
nomes = []
sobrenomes = []
idades = []
alturas = []
pesos = []

# Solicitando os dados dos usuários em um loop
while True:
    logoSenai()
    nome = input("Digite o nome e sobrenome (ou digite 'sair' para encerrar): ")
    sobrenome=input("Digite o nome e sobrenome (ou digite 'sair' para encerrar): ")
    
    # Verificando se o usuário quer sair
    if nome.lower() == 'sair' or sobrenome.lower() == 'sair':
        break

    idade = int(input("Digite a idade do usuário: "))
    altura = float(input("Digite a altura do usuário (em metros): "))
    peso = float(input("Digite o peso do usuário (em quilogramas): "))
    
    # Adicionando os dados às listas
    nomes.append(nome)
    idades.append(idade)
    alturas.append(altura)
    pesos.append(peso)
    sobrenomes.append(sobrenome)
    lista_imc = IMC(alturas,pesos)
    


# Exibindo os dados armazenados
logoSenai()
nivel_obesidade(lista_imc,nomes,idades,sobrenomes,alturas,pesos)
