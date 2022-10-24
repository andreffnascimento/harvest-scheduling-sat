from hsp.hsp import HarvestSchedulingProblem
from hsp.hsp_variables import HSPVariables


class HSPOutput:
    def __init__(self, hsp:HarvestSchedulingProblem, variables:HSPVariables, cost:int) -> None:
        self.hsp = hsp
        self.variables = variables
        self.cost = cost

    def __str__(self) -> str:
        return self.__profit_str() + self.__period_harvested_str() + self.__nature_reserve_str()

    def __profit_str(self) -> str:
        total_harvest = 0
        for i in range(self.hsp.n_areas):
            for t in range(self.hsp.n_periods):
                total_harvest += self.hsp.areas[i].profits[t]
        return str(total_harvest - self.cost) + '\n'

    def __period_harvested_str(self) -> str:
        period_harvested_str = ''
        for t in range(self.hsp.n_periods):
            harvested = ()
            for i in range(self.hsp.n_areas):
                if self.variables.harv[i][t].value:
                    harvested += (str(i + 1),)
            period_harvested_str += str(len(harvested)) + ' ' + ' '.join(harvested) + '\n'
        return period_harvested_str

    def __nature_reserve_str(self) -> str:
        nature_reserves = ()
        for i in range(self.hsp.n_areas):
            if self.variables.nat[i].value:
                nature_reserves += (str(i + 1),)
        return str(len(nature_reserves)) + ' ' + ' '.join(nature_reserves)