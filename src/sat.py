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


class Clause:
    def add_to_formula(self, formula:WCNFPlus) -> WCNFPlus:
        return formula


class HardClause(Clause):
    def __init__(self, variables:tuple[tuple[Variable, bool]]) -> None:
        self.variables = variables

    def add_to_formula(self, formula:WCNFPlus) -> WCNFPlus:
        formula.append(self.variables)
        return formula

    def __str__(self) -> str:
        return str(tuple(('' if sign else '-') + str(variable) for (variable, sign) in self.variables))

    def __repr__(self) -> str:
        return str(tuple(('' if sign else '-') + str(variable) for (variable, sign) in self.variables))


class Solver:
    def __init__(self, variables:tuple[Variable], clauses:tuple[Clause]) -> None:
        self.variables = variables
        self.clauses = clauses
        self.cost = None

    def solve(self) -> None:
        formula = WCNFPlus()
        for variable in self.variables:
            variable.add_to_formula(formula)
        for clause in self.clauses:
            clause.add_to_formula(formula)

        with RC2(formula) as solver:
            result = solver.compute()
            self.cost = solver.cost
            for i in range(len(result)):
                self.variables[i].__result = result[i]