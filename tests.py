from data import MalariaCases
import builddata
import unittest
from main import population_below
from main import population_above
from main import cases_below
from main import cases_above
from main import population_infected
from main import gdppc_below
from main import gdppc_above
from main import change_in_number_cases

#Abhay Sanilnath
class MalariaCasesTestCases(unittest.TestCase):
    pass

    def test_population_below(self):
        a = MalariaCases("India", {2000: 22, 2024: 1}, 2697, 1469300000, "Asia")
        b = MalariaCases("Namibia", {2000: 54, 2024: 7}, 4413, 2600000, "Africa")
        countries = [a, b]
        result = population_below(countries, 10000000)
        self.assertEqual(result, ["Namibia"])

    def test_population_above(self):
        a = MalariaCases("Brazil", {2000: 22, 2024: 15}, 10280, 219000000, "South America")
        b = MalariaCases("Paraguay", {2000: 37, 2024: 0}, 6416, 7400000, "South America")
        countries = [a, b]
        result = population_above(countries, 50000000)
        self.assertEqual(result, ["Brazil"])

    def test_cases_below(self):
        a = MalariaCases("India", {2000: 22, 2024: 1}, 2697, 1469300000, "Asia")
        b = MalariaCases("Somalia", {2000: 133, 2024: 53}, 637, 17100000, "Africa")
        countries = [a, b]
        result = cases_below(countries, 5, 2024)
        self.assertEqual(result, ["India"])

    def test_cases_above(self):
        a = MalariaCases("Sierra Leone", {2000: 425, 2024: 283}, 873, 8600000, "Africa")
        b = MalariaCases("Thailand", {2000: 7, 2024: 1}, 7345, 71700000, "Asia")
        countries = [a, b]
        result = cases_above(countries, 100, 2024)
        self.assertEqual(result, ["Sierra Leone"])

    def test_population_infected(self):
        a = MalariaCases("Uganda", {2000: 483, 2024: 264}, 1072, 48000000, "Africa")
        result = population_infected(a, 2024)
        self.assertEqual(result, 48000000 * 264 // 1000)

    def test_gdppc_below(self):
        a = MalariaCases("Ethiopia", {2000: 189, 2024: 139}, 1011, 134900000, "Africa")
        b = MalariaCases("United Arab Emirates", {2000: 0, 2024: 0}, 49378, 10100000, "Asia")
        countries = [a, b]
        result = gdppc_below(countries, 10000)
        self.assertEqual(result, ["Ethiopia"])

    def test_gdppc_above(self):
        a = MalariaCases("Peru", {2000: 13, 2024: 3}, 8452, 34100000, "South America")
        b = MalariaCases("United Arab Emirates", {2000: 0, 2024: 0}, 49378, 10100000, "Asia")
        countries = [a, b]
        result = gdppc_above(countries, 10000)
        self.assertEqual(result, ["United Arab Emirates"])

    def test_change_in_number_cases(self):
        a = MalariaCases("Tanzania", {2000: 335, 2024: 137}, 1185, 68500000, "Africa")
        result = change_in_number_cases(a, 2000, 2024)
        self.assertEqual(result, -198)




if __name__ == "__main__":
    unittest.main()

