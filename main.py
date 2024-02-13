def calcular_ranked(vitorias, derrotas):
    saldoVitorias = vitorias - derrotas

    if vitorias < 10:
        nivel = "Ferro"
    elif vitorias <= 20:
        nivel = "Bronze"
    elif vitorias <= 50:
        nivel = "Prata"
    elif vitorias <= 80:
        nivel = "Ouro"
    elif vitorias <= 90:
        nivel = "Diamante"
    elif vitorias <= 100:
        nivel = "Lendário"
    else:
        nivel = "Imortal"

    return saldoVitorias, nivel

vitorias = int(input("Digite a quantidade de vitórias: "))
derrotas = int(input("Digite a quantidade de derrotas: "))
saldoVitorias, nivel = calcular_ranked(vitorias, derrotas)

print(f"O Herói tem de saldo de {saldoVitorias} vitórias está no nível de {nivel}")