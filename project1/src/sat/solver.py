from pysat.examples.rc2 import RC2
from pysat.formula import WCNF


class Solver:
    def __init__(self, formula:WCNF) -> None:
        self.formula = formula
        self.result = None
        self.cost = None

    def solve(self) -> tuple[int]|None:
        with RC2(self.formula, solver='gluecard4', adapt=True, exhaust=True, minz=True) as solver:
            result = solver.compute()
            self.cost = solver.cost
            return result