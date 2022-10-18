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
        hsp_soft = '\n[ Clauses: Soft ]:\n'
        for i in range(len(self.formula.soft)):
            literals = [('¬' if var < 0 else '') + self.variables[abs(var)].__repr__() for var in self.formula.soft[i]]
            hsp_soft += ' v '.join(literals) + ' | ' + str(self.formula.wght[i]) + '\n'
        return hsp_formula_str + hsp_hard + hsp_atms + hsp_soft

    def __create_formula(self) -> None:
        self.__maximum_profit()
        self.__adjacent_areas()
        self.__harvest_at_most_once()
        self.__harvest_adjacent_at_same_time()
        self.__nature_reserve_minimum_size()
        self.__nature_reserve_not_harvested()
        self.__nature_reserve_connected()

    def __maximum_profit(self) -> None:
        for i in range(self.hsp.n_areas):
            for t in range(self.hsp.n_periods):
                self.formula.append([self.variables.harv[i][t].id], weight=self.hsp.areas[i].profits[t])

    def __adjacent_areas(self) -> None:
        for i in range(len(self.hsp.areas)):
            for j in range(len(self.hsp.areas)):
                self.formula.append([(1 if self.hsp.areas[j] in self.hsp.areas[i].adjacencies else -1) * self.variables.adj[i][j].id])

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
        clauses = PBEnc.atleast(variables, weights, self.hsp.min_natural_reserve, top_id=len(self.variables)).clauses
        new_variables = ()
        for clause in clauses:
            self.formula.append(clause)
            for variable_id in clause:
                if variable_id > len(self.variables) and variable_id not in new_variables:
                    new_variables += (variable_id,)
        self.variables.add_new_aux_variables(sorted(new_variables))

    def __nature_reserve_not_harvested(self) -> None:
        for i in range(self.hsp.n_areas):
            for t in range(self.hsp.n_periods):
                self.formula.append([-self.variables.nat[i].id, -self.variables.harv[i][t].id])

    def __nature_reserve_connected(self) -> None:
        self.__conn_root_depth()
        self.__conn_root_is_unique_predecessor()
        self.__conn_non_nature_reserve_depth()
        self.__conn_nature_reserve_depth_not_one()
        self.__conn_depth_limit()
        self.__conn_unit_has_depth()
        self.__conn_unit_unique_depth()
        self.__conn_unit_has_unique_predecessor()
        self.__conn_nature_reserve_has_predecessor()
        self.__conn_predecessor_is_adjacent()
        self.__conn_nature_reserve_depth_propagation()

    def __conn_root_depth(self) -> None:
        self.formula.append([self.variables.conn_depth[0][1].id])

    def __conn_root_is_unique_predecessor(self) -> None:
        variables = [self.variables.conn_pred[i][0].id for i in range(self.hsp.n_areas + 1)]
        self.formula.append([variables, 1], is_atmost=True)

    def __conn_non_nature_reserve_depth(self) -> None:
        for i in range(self.hsp.n_areas):
            self.formula.append([self.variables.nat[i].id, self.variables.conn_depth[i + 1][0].id])

    def __conn_nature_reserve_depth_not_one(self) -> None:
        for i in range(self.hsp.n_areas):
            self.formula.append([-self.variables.nat[i].id, -self.variables.conn_depth[i + 1][1].id])
    
    def __conn_depth_limit(self) -> None:
        for i in range(1, self.hsp.n_areas + 1):
            self.formula.append([-self.variables.conn_depth[i][self.hsp.n_areas + 2].id])

    def __conn_unit_has_depth(self) -> None:
        for i in range(1, self.hsp.n_areas + 1):
            variables = [self.variables.conn_depth[i][j].id for j in range(self.hsp.n_areas + 2)]
            self.formula.append(variables)

    def __conn_unit_unique_depth(self) -> None:
        for i in range(1, self.hsp.n_areas + 1):
            variables = [self.variables.conn_depth[i][d].id for d in range(self.hsp.n_areas + 2)]
            self.formula.append([variables, 1], is_atmost=True)

    def __conn_unit_has_unique_predecessor(self) -> None:
        for i in range(self.hsp.n_areas + 1):
            variables = [self.variables.conn_pred[i][j].id for j in range(self.hsp.n_areas + 1)]
            self.formula.append([variables, 1], is_atmost=True)

    def __conn_nature_reserve_has_predecessor(self) -> None:
        for i in range(1, self.hsp.n_areas + 1):
            variables = [self.variables.conn_pred[i][j].id for j in range(self.hsp.n_areas + 1)]
            self.formula.append([-self.variables.nat[i - 1].id] + variables)

    def __conn_predecessor_is_adjacent(self) -> None:
        for i in range(1, self.hsp.n_areas + 1):
            for j in range(1, self.hsp.n_areas + 1):
                self.formula.append([-self.variables.conn_pred[i][j].id, self.variables.adj[i - 1][j - 1].id])

    def __conn_nature_reserve_depth_propagation(self) -> None:
        for i in range(1, self.hsp.n_areas + 1):
            for j in range(self.hsp.n_areas + 1):
                for d in range(self.hsp.n_areas + 2):
                    self.formula.append([-self.variables.conn_pred[i][j].id, -self.variables.conn_depth[j][d].id, self.variables.conn_depth[i][d + 1].id])