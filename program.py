"""Menu de geometria; importar o módulo não inicia o programa."""
from geometry import circle_area, circumference, dimension, rectangle, rhombus, square, trapezoid, triangle


def menu():
    print('\nEscolha o tipo de cálculo:')
    for key, text in [('1', 'Área do triângulo'), ('2', 'Área do quadrado'), ('3', 'Área do trapézio'), ('4', 'Área do círculo'), ('5', 'Área do retângulo'), ('6', 'Área do losango'), ('7', 'Circunferência'), ('0', 'Sair')]:
        print(key + ' - ' + text)


def choice(prompt, options):
    while True:
        answer = input(prompt).strip().casefold()
        if answer in options:
            return answer
        print('Opção inválida. Tente novamente.')


def read_dimension(prompt, unit):
    while True:
        try:
            return dimension(input(prompt), unit)
        except ValueError as error:
            print(error)


def _filtro(value):
    return dimension(value)


def resultado(value):
    text = format(value, '.12g')
    if '.' not in text and 'e' not in text:
        text += '.0'
    return text.replace('.', ',')


def calculate(option, unit):
    if option not in ('1', '2', '3', '4', '5', '6', '7'):
        raise ValueError('Tipo de cálculo inválido')
    read = lambda prompt: read_dimension(prompt, unit)
    if option == '1':
        return triangle(read('Valor da base: '), read('Valor da altura: '))
    if option == '2':
        return square(read('Valor do lado: '))
    if option == '3':
        return trapezoid(read('Valor da base menor: '), read('Valor da base maior: '), read('Valor da altura: '))
    if option == '5':
        return rectangle(read('Valor da base: '), read('Valor da altura: '))
    if option == '6':
        return rhombus(read('Valor da diagonal maior: '), read('Valor da diagonal menor: '))
    method = choice('1 - Utilizando diâmetro; 2 - Utilizando raio: ', ('1', '2'))
    value = read('Valor do diâmetro: ' if method == '1' else 'Valor do raio: ')
    arguments = {'diameter': value} if method == '1' else {'radius': value}
    return circle_area(**arguments) if option == '4' else circumference(**arguments)


def main():
    try:
        while True:
            print('\nUnidade: 1 - cm; 2 - m; 0 - Sair')
            selected = choice('Opção: ', ('0', '1', '2'))
            if selected == '0':
                return
            unit = 'cm' if selected == '1' else 'm'
            menu()
            option = choice('Digite a opção: ', ('0', '1', '2', '3', '4', '5', '6', '7'))
            if option == '0':
                return
            try:
                value = calculate(option, unit)
                print(('Circunferência: ' if option == '7' else 'Área resultante: ') + resultado(value) + ' ' + unit + ('' if option == '7' else '²'))
            except ValueError as error:
                print(error)
            if choice('Deseja realizar outra operação? [S/N]: ', ('s', 'n')) == 'n':
                return
    except (EOFError, KeyboardInterrupt):
        print('\nEncerrando...')


if __name__ == '__main__':
    main()
