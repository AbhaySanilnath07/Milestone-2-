import unittest
import main
import data
from builddata import reduced_data


class TestCases(unittest.TestCase):
    pass

    def test_populationbelow1(self):
        input = reduced_data
        self.assertEqual(main.population_below(input,10000000), ['Namibia', 'Gabon', 'Sierra Leone'])

    def test_populationbelow2(self):
        input = reduced_data
        self.assertEqual(main.population_below(input,20000000), ['Namibia', 'Somalia', 'Gabon', 'Sierra Leone'])

    def test_populationabove1(self):
        input = reduced_data
        self.assertEqual(main.population_above(input,100000000), ['India', 'Democratic Republic of Congo'])

    def test_populationabove2(self):
        input = reduced_data
        self.assertEqual(main.population_above(input,50000000), ['India', 'Myanmar', 'Democratic Republic of Congo'])

    def test_casesbelow1(self):
        input = reduced_data
        self.assertEqual(main.cases_below(input,200, 2000), ['India', 'Namibia', 'Myanmar', 'Somalia', 'Sudan'])

    def test_casesbelow2(self):
        input = reduced_data
        self.assertEqual(main.cases_below(input, 100, 2024), ['India', 'Namibia', 'Myanmar', 'Somalia', 'Sudan'])

    def test_casesabove1(self):
        self.assertEqual(main.cases_above(reduced_data, 400, 2000), ['Sierra Leone', 'Democratic Republic of Congo'])

    def test_casesabove2(self):
        self.assertEqual(main.cases_above(reduced_data, 400, 2024), [])

    def test_populationinfected1(self):
        self.assertEqual(main.population_infected(data.MalariaCases('Myanmar',{2000:34,2024:15},1359,54400000,'Asia'), 2000), 1849600)

    def test_populationinfected2(self):
        self.assertEqual(main.population_infected(data.MalariaCases('Zambia',{2000:360,2024:252},1235,21000000,'Africa'), 2024),5292000)

