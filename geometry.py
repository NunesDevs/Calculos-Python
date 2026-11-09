"""Fórmulas geométricas puras e parser estrito de dimensões positivas."""
import math
import re


def dimension(value, unit=None):
    if unit is not None and unit not in ('cm', 'm'):
        raise ValueError('Unidade inválida; use cm ou m')
    if isinstance(value, bool):
        raise ValueError('Informe uma medida numérica')
    if isinstance(value, str):
        match = re.fullmatch(r'\s*([+-]?(?:\d+(?:[.,]\d*)?|[.,]\d+)(?:[eE][+-]?\d+)?)\s*(cm|m)?\s*', value, re.IGNORECASE)
        if not match:
            raise ValueError('Medida inválida; use número com ponto ou vírgula')
        suffix = match.group(2)
        if suffix and unit and suffix.lower() != unit:
            raise ValueError('Use a unidade selecionada para todas as medidas')
        value = match.group(1).replace(',', '.')
    try:
        number = float(value)
    except (ValueError, TypeError, OverflowError) as error:
        raise ValueError('Informe uma medida numérica') from error
    if not math.isfinite(number) or number <= 0:
        raise ValueError('A medida deve ser positiva e finita')
    return number


def finite_result(value):
    if not math.isfinite(value) or value <= 0:
        raise ValueError('Resultado fora do limite numérico')
    return value


def triangle(base, height):
    return finite_result((dimension(base) / 2) * dimension(height))


def square(side):
    side = dimension(side)
    return finite_result(side * side)


def trapezoid(smaller, larger, height):
    return finite_result((dimension(smaller) / 2 + dimension(larger) / 2) * dimension(height))


def rectangle(base, height):
    return finite_result(dimension(base) * dimension(height))


def rhombus(larger, smaller):
    return finite_result((dimension(larger) / 2) * dimension(smaller))


def radius_from(*, radius=None, diameter=None):
    if (radius is None) == (diameter is None):
        raise ValueError('Informe apenas raio ou diâmetro')
    return dimension(radius) if radius is not None else dimension(diameter) / 2


def circle_area(*, radius=None, diameter=None):
    radius = radius_from(radius=radius, diameter=diameter)
    return finite_result(math.pi * radius * radius)


def circumference(*, radius=None, diameter=None):
    return finite_result(2 * math.pi * radius_from(radius=radius, diameter=diameter))
