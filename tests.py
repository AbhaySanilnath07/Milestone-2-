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
        a = MalariaCases("Aland", {2000: 10, 2024: 5}, 1000, 500_000, "Europe")
        b = MalariaCases("Bolia", {2000: 20, 2024: 10}, 2000, 2_000_000, "Asia")
        countries = [a, b]
        result = population_below(countries, 1000000)
        self.assertEqual(result, ["Aland"])

    def test_population_above(self):
        a = MalariaCases("Brazil", {2000: 80, 2024: 40}, 9000, 210000000, "South America")
        b = MalariaCases("Iceland", {2000: 0, 2024: 0}, 50000, 370000, "Europe")
        countries = [a, b]
        result = population_above(countries, 1000000)
        self.assertEqual(result, ["Brazil"])

    def test_cases_below(self):
        a = MalariaCases("India", {2000: 200, 2024: 100}, 2500, 1400000000, "Asia")
        b = MalariaCases("Japan", {2000: 5, 2024: 2}, 42000, 125000000, "Asia")
        countries = [a, b]
        result = cases_below(countries, 50, 2024)
        self.assertEqual(result, ["Japan"])

    def test_cases_above(self):
        a = MalariaCases("Nigeria", {2000: 300, 2024: 150}, 2200, 220000000, "Africa")
        b = MalariaCases("France", {2000: 3, 2024: 1}, 45000, 67000000, "Europe")
        countries = [a, b]
        result = cases_above(countries, 100, 2024)
        self.assertEqual(result, ["Nigeria"])

    def test_population_infected(self):
        a = MalariaCases("Uganda", {2000: 120, 2024: 60}, 1800, 48000000, "Africa")
        result = population_infected(a, 2024)
        self.assertEqual(result, 48000000 * 60 // 1000)

    def test_gdppc_below(self):
        a = MalariaCases("Ethiopia", {2000: 50, 2024: 30}, 900, 120000000, "Africa")
        b = MalariaCases("Germany", {2000: 2, 2024: 1}, 50000, 83000000, "Europe")
        countries = [a, b]
        result = gdppc_below(countries, 10000)
        self.assertEqual(result, ["Ethiopia"])

    def test_gdppc_above(self):
        a = MalariaCases("Peru", {2000: 40, 2024: 20}, 7000, 33000000, "South America")
        b = MalariaCases("United States", {2000: 1, 2024: 0}, 65000, 330000000, "North America")
        countries = [a, b]
        result = gdppc_above(countries, 10000)
        self.assertEqual(result, ["United States"])

    def test_change_in_number_cases(self):
        a = MalariaCases("Tanzania", {2000: 80, 2024: 50}, 1200, 65000000, "Africa")
        result = change_in_number_cases(a, 2000, 2024)
        self.assertEqual(result, -30)




if __name__ == "__main__":
    unittest.main()

