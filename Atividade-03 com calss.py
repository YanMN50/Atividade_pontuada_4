import os
from dataclasses import dataclass
os.system("cls || clear")

@dataclass
class Cliente:
    nome: str
    idade: int
    altura: float
    peso: float

@dataclass
class Final:
    lista_final: list



def limpar_tela():
    os.system("cls || clear ")

def menu ():
    print("="*40)
    print(f"{"Senai":^40}")
    print("="*40)

    print("""
1. Adicionar família          
2. Exibir os resultados          
3. Sair             
          """)    
    
def criando_arquivo(a,b):
    with open(a, "a") as lista_cliente:
        for cliente in b:
            lista_cliente.write(f"{cliente.nome},{cliente.idade},{cliente.altura},{cliente.peso}\n")
        lista_cliente.close()

def criando_arquivo_final(a,b):
    with open(a, "w") as lista_cliente:
        for cliente in b:
            lista_cliente.write(f"{cliente},\n")
        lista_cliente.close()

def lendo_arquivo(a):
    lista_cliente = []
    with open(a, "r") as arquivo_cliente:
        for linha in arquivo_cliente:
            nome, idade, altura, peso = linha.strip().split(",")
            lista_cliente.append(Cliente (nome = (nome), idade = int(idade), altura = float(altura), peso = float(peso)))
    return lista_cliente



def calculando_imc(clientes):
    lista_imc = []
    for cliente in clientes:
        imc = cliente.peso / cliente.altura**2
        lista_imc.append(imc)
    return lista_imc


def analisando_imc(a:float):
    lista_analise_imc = []

    for cliente in a:
        if cliente >= 40:
            lista_analise_imc.append("Obesidade grau 3")
        elif cliente >= 35:
            lista_analise_imc.append("Obesidade grau 2")
        elif cliente >= 30:
            lista_analise_imc.append("Obesidade grau 1")
        elif cliente >= 25:
            lista_analise_imc.append("Sobrepeso")
        elif cliente >=18.5:
            lista_analise_imc.append("Peso normal")
        elif cliente <= 18.5:
            lista_analise_imc.append("Abaixo do peso")

    return lista_analise_imc

lista_cliente = []

while True:
    menu()
    opcao = input("Resposta: ")
    match opcao:
        case "1":
            cliente = Cliente(
                nome = input("Digite seu nome: "),
                idade = int(input("Digite sua idade: ")),
                altura = float(input("Digite sua altura: ")),
                peso = float(input("Digite seu peso: "))
            )
            lista_cliente.append(cliente)
            nome_arquivo = "Dados.txt"
            criando_arquivo(nome_arquivo, lista_cliente)
            limpar_tela()
        case "2":
            limpar_tela()
            nome_arquivo = "Dados.txt"
            lista_definitiva = lendo_arquivo(nome_arquivo)
            imc = calculando_imc(lista_definitiva)
            analise_imc = analisando_imc(imc)
            nome_arquivo1 = "pesquisa_IMC.txt"
            criando_arquivo_final(nome_arquivo1, imc)
            print("="*40)
            print(f"{"Resultado":^40}")
            print("="*40)
            for i, cliente in enumerate(lista_definitiva):
                print(f"\nNome: {cliente.nome}")
                print(f"Idade: {cliente.idade}")
                print(f"Altura: {cliente.altura}")
                print(f"Peso: {cliente.peso}")
                print(f"Seu IMC é: {imc[i]:.2f}")
                print(f"Grau: {analise_imc[i]}")

        case "3":
            break
            
        case _:
            print("Opção inválida")
            continue
            
            
            
