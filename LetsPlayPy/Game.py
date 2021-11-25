from Models.Calcular import Calcular

def main() -> None:
    points: int = 0
    play(points)


def play(points: int) -> None:
    dificulty: int = int(input('Select dificulty: [1] | [2] | [3] | [4]'))

    calc: Calcular = Calcular(dificulty)
    print('Inform the result of the following operation: ')
    calc.show_operation()
    result: int = int(input())

    if calc.check_result(result):
        points += 1
        print(f'You have {points} points.')

    proceed: int = int(input('Do you want to continue the game? [1] - yes | [0] - no'))

if __name__ == '__main__':
    main()