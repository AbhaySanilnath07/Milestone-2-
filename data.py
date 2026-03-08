class MalariaCases:
    def __init__(self, name:str, cases:dict[str, int], gdppc:int, population:int, continent:str):
        self.name = name
        self.cases = cases
        self.gdppc = gdppc
        self.population = population
        self.continent = continent

    def __repr__(self):
        return 'MalariaCases({}, {}, {}, {}, {})'.format(
            self.name, self.cases, self.gdppc, self.population, self.continent
        )

    def __eq__(self, other):
        if not isinstance(other, MalariaCases):
            return False

        return (
                self.name == other.name and
                self.cases == other.cases and
                self.gdppc == other.gdppc and
                self.population == other.population and
                self.continent == other.continent
        )