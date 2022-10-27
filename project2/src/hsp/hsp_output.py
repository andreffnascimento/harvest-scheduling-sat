from z3 import ModelRef

from hsp.hsp import HarvestSchedulingProblem
from hsp.hsp_variables import HSPVariables


class HSPOutput:
    def __init__(self, hsp:HarvestSchedulingProblem, vars:HSPVariables, model:ModelRef) -> None:
        self.hsp = hsp
        self.vars = vars
        self.model = model

    def __str__(self) -> str:
        return self.__profit_str() + self.__period_harvested_str() + self.__nature_reserve_str()

    def variable_values(self) -> str:
        hsp_variables = ('=' * 80) + '\n\tVariable Results\n' + ('=' * 80) + '\n'
        for var in self.vars.get_variables():
            hsp_variables += f'{str(var)} = {self.model[var]}\n'
        return hsp_variables

    def __profit_str(self) -> str:
        profit = sum([int(str(self.model[var])) for var in self.vars.prof])
        return str(profit) + '\n'

    def __period_harvested_str(self) -> str:
        period_harvested_str = ''
        for t in range(self.hsp.n_periods):
            harvested = tuple(map(lambda name: str(name)[5:], filter(lambda var: self.model[var] == t, self.vars.harv)))
            period_harvested_str += str(len(harvested)) + ' ' + ' '.join(harvested) + '\n'
        return period_harvested_str

    def __nature_reserve_str(self) -> str:
        nature_reserves = tuple(map(lambda name: str(name)[4:], filter(lambda var: not(self.model[var] == -1), self.vars.nat)))
        return str(len(nature_reserves)) + ' ' + ' '.join(nature_reserves)