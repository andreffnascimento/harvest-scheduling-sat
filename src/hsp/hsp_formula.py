from pysat.formula import WCNFPlus
from pysat.pb import PBEnc

from hsp.hsp import HarvestSchedulingProblem
from hsp.hsp_variables import HSPVariables


class HSPFormula:
    def __init__(self, hsp:HarvestSchedulingProblem, variables:HSPVariables) -> None:
        self.hsp = hsp
        self.variables = variables
        self.formula = WCNFPlus()
        self.__create_formula()

    def __str__(self) -> str:
        hsp_formula_str = ('=' * 80) + '\n\tFormula\n' + ('=' * 80) + '\n'
        hsp_hard = '\n[ Clauses: Hard ]:\n'
        for clause in self.formula.hard:
            literals = [('¬' if var < 0 else '') + self.variables[abs(var)].__repr__() for var in clause]
            hsp_hard += ' v '.join(literals) + '\n'
        hsp_atms = '\n[ Clauses: AtMost ]:\n'
        for clause in self.formula.atms:
            literals = [('-' if var < 0 else '') + self.variables[abs(var)].__repr__() for var in clause[0]]
            hsp_atms += ' + '.join(literals) + ' ≤ ' + str(clause[1]) + '\n'
        return hsp_formula_str + hsp_hard + hsp_atms

    def __create_formula(self) -> None:
        self.__harvest_at_most_once()
        self.__harvest_adjacent_at_same_time()
        self.__nature_reserve_minimum_size()
        self.__nature_reserve_not_harvested()
        self.__nature_reserve_connected()

    def __harvest_at_most_once(self) -> None:
        for i in range(self.hsp.n_areas):
            variables = [self.variables.harv[i][t].id for t in range(self.hsp.n_periods)]
            self.formula.append([variables, 1], is_atmost=True)

    def __harvest_adjacent_at_same_time(self) -> None:
        for i in range(self.hsp.n_areas):
            for j in range(self.hsp.n_areas):
                for t in range(self.hsp.n_periods):
                    self.formula.append([-self.variables.adj[i][j].id, -self.variables.harv[i][t].id, -self.variables.harv[j][t].id])

    def __nature_reserve_minimum_size(self) -> None:
        variables = [self.variables.nat[i].id for i in range(self.hsp.n_areas)]
        weights = [area.size for area in self.hsp.areas]
        for clause in PBEnc.atleast(variables, weights, self.hsp.min_natural_reserve).clauses:
            self.formula.append(clause)

    def __nature_reserve_not_harvested(self) -> None:
        for i in range(self.hsp.n_areas):
            for t in range(self.hsp.n_periods):
                self.formula.append([-self.variables.nat[i].id, -self.variables.harv[i][t].id])

    def __nature_reserve_connected(self) -> None:
        pass    # TODO

# def connected_nature_reserve(hsp:HarvestSchedulingProblem, variables:dict, formula:WCNFPlus) -> None:
#     adj_variables  = variables['Adj']
#     nat_variables = variables['Nat']
#     conn_variables = variables['Conn']
#     for i in range(hsp.n_areas):
#         for j in range(hsp.n_areas):
#             formula.append([nat_variables[i].id, -conn_variables[i][j].id])
#             formula.append([nat_variables[j].id, -conn_variables[i][j].id])
#             formula.append([-nat_variables[i].id, -nat_variables[j].id, -adj_variables[i][j].id, conn_variables[i][j].id])
#             formula.append([-nat_variables[i].id, -nat_variables[j].id, conn_variables[i][j].id])