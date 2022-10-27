from z3 import *

from hsp.hsp import HarvestSchedulingProblem
from hsp.hsp_variables import HSPVariables


class HSPFormula:
    def __init__(self, hsp:HarvestSchedulingProblem, vars:HSPVariables) -> None:
        self.hsp = hsp
        self.vars = vars
        self.solver = Optimize()
        self.__create_formula()

    def get_solver(self) -> Optimize:
        return self.solver

    def __create_formula(self) -> None:
        self.__maximum_profit()
        self.__harvest_period_bound()
        self.__harvest_profit_relation()
        self.__harvest_adjacent_at_same_time()
        self.__nature_reserve_depth_bound()
        self.__nature_reserve_size_relation()
        self.__nature_reserve_not_harvested()
        self.__nature_reserve_minimum_size()

    def __maximum_profit(self) -> None:
        self.solver.maximize(Sum(self.vars.prof))

    def __harvest_period_bound(self) -> None:
        for i in range(self.hsp.n_areas):
            self.solver.add(self.vars.harv[i] >= IntVal(0))
            self.solver.add(self.vars.harv[i] <= IntVal(str(self.hsp.n_periods)))

    def __harvest_profit_relation(self) -> None:
        for i in range(self.hsp.n_areas):
            self.solver.add(Implies(self.vars.harv[i] == IntVal("0"), self.vars.prof[i] == IntVal("0")))
            for t in range(self.hsp.n_periods):
                profit = self.hsp.areas[i].profits[t]
                self.solver.add(Implies(self.vars.harv[i] == IntVal(str(t + 1)), self.vars.prof[i] == IntVal(str(profit))))

    def __harvest_adjacent_at_same_time(self) -> None:
        for i in range(self.hsp.n_areas):
            for adj in self.hsp.areas[i].adjacencies:
                self.solver.add(self.vars.harv[i] != self.vars.harv[adj.id - 1])

    def __nature_reserve_depth_bound(self) -> None:
        for i in range(self.hsp.n_areas):
            self.solver.add(self.vars.nat[0] >= IntVal('-1'))
            self.solver.add(self.vars.nat[0] <= IntVal(str(self.hsp.max_nature_reserve_depth)))

    def __nature_reserve_size_relation(self) -> None:
        for i in range(self.hsp.n_areas):
            area_size = self.hsp.areas[i].size
            self.solver.add(Implies(self.vars.nat[i] == IntVal('-1'), self.vars.natsize[i] == IntVal('0')))
            self.solver.add(Implies(self.vars.nat[i] != IntVal('-1'), self.vars.natsize[i] == IntVal(str(area_size))))

    def __nature_reserve_not_harvested(self) -> None:
        for i in range(self.hsp.n_areas):
            self.solver.add(Implies(self.vars.nat[i] != IntVal('-1'), self.vars.harv[i] == IntVal('0')))

    def __nature_reserve_minimum_size(self) -> None:
        self.solver.add(Sum(self.vars.natsize) >= IntVal(str(self.hsp.min_nature_reserve_area)))