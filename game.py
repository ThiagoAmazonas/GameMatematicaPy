from models.calcular import Calcular


def main() -> None:
    pontos: int = 0
    jogar(pontos)


def jogar(pontos: int) -> None:
    dificuldade: int = int(input('Informe o nível de difculdade desejado [1, 2, 3 ou 4]: '))

    calc: Calcular = Calcular(dificuldade)

    print('Informe o resultado para a seguinte operaçao: ')
    calc.mostrar_operacao()

    resultado: int = int(input())

    if calc.checar_resultado(resultado):
        pontos += 1
        print(f'Voce tem {pontos} ponto(s)')

    continuar: int = int(input('Deseja continuar no jogo? [1 - sim, 0 - nao]'))

    while continuar != 1 and continuar != 0:
        print("Apenas, 1 - Sim ou 0 - Nao")
        continuar: int = int(input('Deseja continuar no jogo? [1 - sim, 0 - nao]'))
    if continuar == 1:
        jogar(pontos)
    elif continuar == 0:
        print(f'Voce finalizou com {pontos} ponto(s).')
        print('Até a próxima')


if __name__ == '__main__':
    main()
