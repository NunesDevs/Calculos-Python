import os
from pathlib import Path
import subprocess
import sys
import unittest


class CalculatorRegressionTests(unittest.TestCase):
    def calculate(self, answers):
        result = subprocess.run(
            [sys.executable, "program.py"],
            cwd=Path(__file__).resolve().parents[1],
            input=answers,
            text=True,
            encoding="utf-8",
            capture_output=True,
            timeout=5,
            env={**os.environ, "PYTHONIOENCODING": "utf-8"},
        )
        self.assertEqual(result.returncode, 0, result.stderr)
        return result.stdout

    def test_square_runs_without_optional_curses(self):
        self.assertIn("16,0", self.calculate("1\n2\n4\nN\n"))

    def test_circle_diameter_prints_calculated_result(self):
        self.assertIn("78,539816", self.calculate("1\n4\n1\n10\nN\n"))

    def test_previously_missing_shapes_and_other_menu_paths(self):
        for answers, expected in [
            ('1\n1\n4\n3\nn\n', '6,0 cm²'),
            ('1\n3\n2\n4\n3\nn\n', '9,0 cm²'),
            ('2\n5\n4\n3\nn\n', '12,0 m²'),
            ('1\n6\n8\n6\nn\n', '24,0 cm²'),
            ('1\n4\n2\n5\nn\n', '78,539816'),
            ('1\n7\n1\n10\nn\n', '31,415926'),
            ('1\n7\n2\n5\nn\n', '31,415926'),
        ]:
            self.assertIn(expected, self.calculate(answers))

    def test_invalid_menu_dimension_and_unit_recover_and_eof_exits(self):
        output = self.calculate('x\n1\ninvalid\n2\nNaN\n2m\n4cm\nn\n')
        self.assertIn('16,0 cm²', output)
        self.assertIn('Opção inválida', output)
        self.assertIn('unidade selecionada', output)
        self.assertIn('Encerrando', self.calculate(''))

    def test_import_has_no_interactive_side_effect(self):
        result = subprocess.run([sys.executable, '-X', 'utf8', '-c', 'import program; print("import-ok")'], cwd=Path(__file__).resolve().parents[1], input='', text=True, encoding='utf-8', capture_output=True, timeout=5)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(result.stdout.strip(), 'import-ok')


if __name__ == "__main__":
    unittest.main()
