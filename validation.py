import unittest
from unittest.mock import patch
from io import StringIO
#from coffee_machine import coffee_machine

class TestCoffeeMachine(unittest.TestCase):
    @patch('builtins.input', side_effect=['report'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_print_report(self, mock_stdout, mock_input):
        expected_output = "Water: 300ml\nMilk: 200ml\nCoffee: 100g\nMoney: $0\n"
        coffee_machine()
        self.assertEqual(mock_stdout.getvalue(), expected_output)

if __name__ == '__main__':
    unittest.main()
