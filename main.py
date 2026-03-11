from data import MalariaCases
#Rafael Bustos
def population_below(lst:list[MalariaCases], pop:int):
    return [i.name for i in lst if i.population < pop]

def population_above(lst:list[MalariaCases], pop:int):
    return [i.name for i in lst if i.population > pop]

def cases_below(lst:list[MalariaCases], amt:int, year:float):
    return [i.name for i in lst if i.cases[year] < amt]

def cases_above(lst:list[MalariaCases], amt:int, year:int):
    return [i.name for i in lst if i.cases[year] > amt]

def population_infected(country:MalariaCases, year:int):
    return country.population * country.cases[year] // 1000
#Abhay Sanilnath
def gdppc_below(lst:list[MalariaCases], amt:int):
    return [i.name for i in lst if i.gdppc < amt]

def gdppc_above(lst:list[MalariaCases], amt:int):
    return [i.name for i in lst if i.gdppc > amt]

def change_in_number_cases(country: MalariaCases, year1:int, year2:int):
    return country.cases[year2] - country.cases[year1]

