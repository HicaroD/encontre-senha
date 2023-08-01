import random
import string


def gerar_individuo():
    caracteres = string.ascii_uppercase + string.digits
    return "".join(random.choice(caracteres) for _ in range(10))


def calcular_aptidao(individuo, senha_desejada):
    return sum(1 for a, b in zip(individuo, senha_desejada) if a == b)


def crossover(individuo1, individuo2):
    ponto_corte = random.randint(1, 6)
    novo_individuo = individuo1[:ponto_corte] + individuo2[ponto_corte:]
    return novo_individuo


def mutacao(individuo):
    caracteres = string.ascii_uppercase + string.digits
    posicao_mutacao = random.randint(0, 9)
    novo_caractere = random.choice(caracteres)
    novo_individuo = (
        individuo[:posicao_mutacao] + novo_caractere + individuo[posicao_mutacao + 1 :]
    )
    return novo_individuo


def encontrar_senha(senha_desejada):
    tamanho_populacao = 50
    taxa_mutacao = 0.1
    geracoes = 10000

    populacao = [gerar_individuo() for _ in range(tamanho_populacao)]

    for geracao in range(geracoes):
        aptidoes = [
            calcular_aptidao(individuo, senha_desejada) for individuo in populacao
        ]
        melhor_individuo = populacao[aptidoes.index(max(aptidoes))]

        print(f"Geracao {geracao}: Melhor Individuo: {melhor_individuo}")

        if melhor_individuo == senha_desejada:
            print("Senha encontrada!")
            break

        proxima_geracao = []

        for _ in range(tamanho_populacao // 2):
            pai = random.choices(populacao, weights=aptidoes)[0]
            mae = random.choices(populacao, weights=aptidoes)[0]

            filho = crossover(pai, mae)

            if random.random() < taxa_mutacao:
                filho = mutacao(filho)

            proxima_geracao.append(filho)

        populacao = proxima_geracao


def main():
    senha_desejada = "ABCDEFGHIJ"
    encontrar_senha(senha_desejada)


if __name__ == "__main__":
    main()
