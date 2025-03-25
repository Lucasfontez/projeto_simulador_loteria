import random
from collections import Counter
import matplotlib.pyplot as plt

def sortear_apostas(total_apostas, max_numero, quantidade_por_aposta):
    apostas = []
    for _ in range(total_apostas):
        aposta = random.sample(range(1, max_numero + 1), quantidade_por_aposta)
        apostas.append(sorted(aposta))
    return apostas

def analisar_frequencia(apostas):
    numeros = [num for aposta in apostas for num in aposta]
    frequencias = Counter(numeros)
    return frequencias

def plotar_frequencia(frequencias):
    numeros = list(frequencias.keys())
    contagens = list(frequencias.values())

    plt.bar(numeros, contagens)
    plt.xlabel("Números Sorteados")
    plt.ylabel("Frequência")
    plt.title("Frequência dos Números Sorteados")
    plt.show()

def main():
    print("Simulador de Loteria")
    
    # Parâmetros de entrada
    total_apostas = int(input("Quantas apostas você quer simular? "))
    max_numero = int(input("Qual o maior número do sorteio (ex: 60)? "))
    quantidade_por_aposta = int(input("Quantos números por aposta? (ex: 6) "))
    
    # Sorteio
    apostas = sortear_apostas(total_apostas, max_numero, quantidade_por_aposta)
    
    # Exibição dos resultados das apostas
    print("\nApostas sorteadas:")
    for aposta in apostas:
        print(aposta)
    
    # Análise de frequência
    frequencias = analisar_frequencia(apostas)
    print("\nFrequência dos números sorteados:")
    for numero, contagem in sorted(frequencias.items()):
        print(f"Número {numero}: {contagem} vez(es)")
    
    # Gráfico
    plotar_frequencia(frequencias)

if __name__ == "__main__":
    main()
