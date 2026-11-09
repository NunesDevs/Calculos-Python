import math
import unittest
from geometry import circle_area, circumference, dimension, rectangle, rhombus, square, trapezoid, triangle


class GeometryTests(unittest.TestCase):
    def test_all_area_formulas(self):
        self.assertEqual(triangle(4, 3), 6)
        self.assertEqual(square(4), 16)
        self.assertEqual(trapezoid(2, 4, 3), 9)
        self.assertEqual(rectangle(4, 3), 12)
        self.assertEqual(rhombus(8, 6), 24)
        self.assertAlmostEqual(circle_area(radius=5), math.pi * 25)
        self.assertEqual(circle_area(radius=5), circle_area(diameter=10))
        self.assertEqual(circumference(radius=5), circumference(diameter=10))

    def test_dimension_parser_validates_numbers_and_units(self):
        self.assertEqual(dimension(' 2,5 cm ', 'cm'), 2.5)
        self.assertEqual(dimension('.5m', 'm'), 0.5)
        self.assertEqual(dimension('2e2', 'cm'), 200)
        for value in ('2abc', '1,2.3', 'NaN', 'Infinity', '', 0, -1, True, None, float('inf')):
            with self.assertRaises(ValueError):
                dimension(value)
        with self.assertRaisesRegex(ValueError, 'unidade selecionada'):
            dimension('2m', 'cm')

    def test_invalid_and_out_of_range_geometry(self):
        for function, values in [(triangle, [1, -1]), (square, [0]), (rectangle, [1e308, 1e308]), (rhombus, [1e308, 1e308])]:
            with self.assertRaises(ValueError):
                function(*values)
        for kwargs in ({}, {'radius': 1, 'diameter': 2}, {'radius': 0}, {'diameter': -1}, {'radius': 1e308}):
            with self.assertRaises(ValueError):
                circle_area(**kwargs)


if __name__ == '__main__':
    unittest.main()
