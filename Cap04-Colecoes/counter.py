# Usando a classe counter
from collections import Counter


def main():
    turma_a = ["Barbara", "João", "Carlos", "Dario", "Priscila", "Ana"
               "Kevin", "João", "Marina", "Bianca", "Gustavo",
               "Fernanda"]

    turma_b = ["Hiro", "Bruno", "Claudia", "Debora", "Fernanda",
               "Gabriela", "Leticia", "João", "Jairo", "Samuel",
               "Taciana", "Gabriel"]

    # Criando counter para as turmas
    a = Counter(turma_a)
    b = Counter(turma_b)

    # TODO: Quantos estudantes na turma A se chamam joão?
    print(a["João"])

    # TODO: Quantos estudantes  estão na turma A?
    print(sum(a.values()))

    # TODO: Combine as duas turmas
    a.update(turma_b)
    print(sum(a.values()))

    # TODO: Quas os 3 nomes mais comuns nas duas turmas?
    print(a.most_common())

    # Separando as turmas
    a.subtract(turma_b)
    print(a.most_common(3))

    # TODO: Qual a intersecção de nome entre as duas turmas?
    print(a & b)

main()