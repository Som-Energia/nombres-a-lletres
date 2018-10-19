#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Author: AxiaCore S.A.S. http://axiacore.com
UNIDADES = (
    '',
    'un ',
    'dos ',
    'tres ',
    'quatre ',
    'cinc ',
    'sis ',
    'set ',
    'vuit ',
    'nou ',
    'deu ',
    'onze ',
    'dotze ',
    'tretze ',
    'catorze ',
    'quinze ',
    'setze ',
    'diset ',
    'divuit ',
    'dinou ',
    'vint ',
)

UNIDADES_TILDES = {
}

DECENAS = (
    'vint',
    'trenta',
    'quaranta',
    'cinquanta',
    'seixanta',
    'setanta',
    'vuitanta',
    'noranta',
    'cent ',
)
CENTENAS = (
    'cent ',
    'dos-cents ',
    'tres-cents ',
    'quatre-cents ',
    'cinc-cents ',
    'sis-cents ',
    'set-cents ',
    'vuit-cents ',
    'nou-cents ',
)


def number_to_letters(number):
    """Converts a number into string representation
    """
    converted = ''

    if isinstance(number, str):
        try:
            number = float(number)
        except ValueError:
            raise Exception('El valor ingressat es invàlid')
    number, decimals = ('%.2f' % number).split('.')

    number = int(number)
    decimals = int(decimals)
    negative = number < 0
    if negative:
        number = abs(number)
    if not (0 <= number < 999999999):
        return 'No es possible convertir el número a lletres'

    number_str = str(number).zfill(9)
    millones = number_str[:3]
    miles = number_str[3:6]
    cientos = number_str[6:]

    if millones:
        if millones == '001':
            converted += 'un milió '
        elif int(millones) > 0:
            converted += '{}milions '.format(__convert_number(millones))

    if miles:
        if miles == '001':
            converted += 'mil '
        elif int(miles) > 0:
            converted += '{}mil '.format(__convert_number(miles))

    if cientos:
        if cientos == '001':
            converted += 'un '
        elif int(cientos) > 0:
            converted += __convert_number(cientos)
    if not number:
        converted = 'cero '

    if decimals:
        if converted.endswith('un '):
            converted = converted.replace('un ', ' uno ')
        elif converted.endswith('ún '):
            converted = converted.replace('ún ', ' uno ')
        decimals = number_to_letters(decimals)
        converted += 'amb {}'.format(decimals)
    if negative:
        converted = 'menos {}'.format(converted)
    return converted.strip()


def __convert_number(n):
    """Max length must be 3 digits
    """
    output = ''
    print n
    if n == '100':
        output = 'cent '
    elif n[0] != '0':
        output = CENTENAS[int(n[0]) - 1]

    k = int(n[1:])
    if k <= 20:
        output += UNIDADES[k]
    else:
        decenas = DECENAS[int(n[1]) - 2]
        print decenas
        unidades = UNIDADES[int(n[2])]

        if decenas == 'vint':
            output += '{}-i-{}'.format(decenas, unidades)
        elif (k > 30) & (n[2] != '0'):
            output += '{}-{}'.format(decenas, unidades)
        else:
            output += '{}{}'.format(decenas, unidades)

    return output