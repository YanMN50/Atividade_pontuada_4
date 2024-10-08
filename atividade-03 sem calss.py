import os

# Função sem retorno.
def logoSenai():
    os.system("cls || clear")
    print("="*40)
    print(f"{"Senai":^40}")
    print("="*40)


# Definindo listas vazias para armazenar os dados dos usuários
nomes = []
sobrenomes = []
idades = []
alturas = []
pesos = []

# Solicitando os dados dos usuários em um loop
while True:
    logoSenai()
    nome = input("Digite o nome do usuário (ou digite 'sair' para encerrar): ")
    
    # Verificando se o usuário quer sair
    if nome.lower() == 'sair':
        break
    
    sobrenome = input("Digite seu sobrenome: ")
    idade = int(input("Digite a idade do usuário: "))
    altura = float(input("Digite a altura do usuário (em metros): "))
    peso = float(input("Digite o peso do usuário (em quilogramas): "))
    
    # Adicionando os dados às listas
    nomes.append(nome)
    sobrenomes.append(sobrenome)
    idades.append(idade)
    alturas.append(altura)
    pesos.append(peso)
    



def calculando_imc(a,b):
    lista_imc = []
    for i,peso in enumerate(a):
        imc = peso/(b[i])**2
        lista_imc.append(imc)
    return lista_imc



def analisando_imc(a):
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
        else:
            lista_analise_imc.append("Abaixo do peso")

    return lista_analise_imc
    

imc = calculando_imc(pesos, alturas)
analise_imc = analisando_imc(imc)

# Exibindo os dados armazenados
logoSenai()
print("="*40)
print(f"{"Resultado":^40}")
print("="*40)
for i in range(len(nomes)):
    print(f"Nome: {nomes[i]}")
    print(f"Sobrenome: {sobrenomes[i]}")
    print(f"Idade: {idades[i]}")
    print(f"Altura: {alturas[i]}")
    print(f"Peso: {pesos[i]}")
    print(f"Seu IMC é: {imc[i]:.2f}")
    print(f"Grau: {analise_imc[i]}")