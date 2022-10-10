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
        self.__result = value

    def add_to_formula(self, formula:WCNFPlus) -> WCNFPlus:
        if self.value != None:
            formula.append([self.id * (1 if self.value else -1)])
        return formula

    def result(self) -> str:
        return self.description + '=' + str(self.__result)

    def __str__(self) -> str:
        return self.description

    def __repr__(self) -> str:
        return self.description

class Solver:
    def __init__(self, variables:tuple[Variable]) -> None:
        self.variables = variables
        self.cost = None

    def solve(self, formula:WCNFPlus) -> None:
        with RC2(formula, solver='gluecard4') as solver:
            result = solver.compute()
            self.cost = solver.cost
            for i in range(len(result)):
                self.variables[i].__result = result[i]