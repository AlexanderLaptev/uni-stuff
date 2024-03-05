numerals = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]


def read_numbers():
    numbers = []
    with open('in4.txt') as file:
        for line in file:
            line = line.strip()
            if not line:
                continue

            numbers.extend(line.split())

    return numbers


def convert(number):
    if any(c in number for c in 'IVXLCDM'):
        return convert_decimal(number)
    else:
        return convert_roman(number)


def convert_decimal(roman):
    pass

def convert_roman(decimal):
    decimal = int(decimal)
    if decimal > 3999:
        raise ValueError('Number is too big')

    output = []
    i = 0
    while decimal: # 2463
        count = decimal // values[i]
        decimal %= values[i]
        output.append(numerals[i] * count)
        i += 1
    return ''.join(output)


print(convert_roman('671'))

