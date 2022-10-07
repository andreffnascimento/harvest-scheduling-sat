from pysat.examples.rc2 import RC2
from pysat.formula import WCNFPlus


class VariableGenerator:
    current_id = 1

    def __init__(self) -> None:
        VariableGenerator.current_id = 1

    @staticmethod
    def generate_var():
        id = VariableGenerator.current_id
        VariableGenerator.current_id += 1
        return id


class Variable:
    def __init__(self, description:str, value:bool = None) -> None:
        self.id = VariableGenerator.generate_var()
        self.description = description
        self.value = value
        self.result = None

    def __str__(self) -> str:
        return self.description

    def add_as_clause(self, formula:WCNFPlus) -> WCNFPlus:
        if self.value != None:
            formula.append([self.id * (1 if self.value else -1)])
        return formula


class Solver:
    def __init__(self, variables:tuple[Variable]) -> None:
        self.variables = variables
        self.cost = None

    def solve(self) -> None:
        formula = WCNFPlus()
        for variable in self.variables:
            variable.add_as_clause(formula)

        # Temporary solver
        with RC2(formula) as solver:
            print(solver.compute())
            self.cost = solver.cost
            print('Cost = ' + str(self.cost))
            # Set the result value for each variable