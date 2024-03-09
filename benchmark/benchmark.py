
if __name__ == '__main__':
    # Lê para todos
    with open('binpack1.txt', 'r') as f:
        qtd = int(f.readline())
        for _ in range(qtd):
            f.readline()  # problema

            C, M, otimo = tuple(map(lambda x: int(x), f.readline().split()))

            S = []  # pesos
            for _ in range(M):
                S.append(int(f.readline()))

            individuo = list(range(0, M))

            # EXECUTA PROBLEMA
