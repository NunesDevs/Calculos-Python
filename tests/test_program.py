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
        self.assertIn("78,5375", self.calculate("1\n4\n1\n10\nN\n"))


if __name__ == "__main__":
    unittest.main()
