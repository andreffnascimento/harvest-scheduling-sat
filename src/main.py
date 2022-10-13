from hsp.hsp import HarvestSchedulingProblem
from hsp.hsp_formula import HSPFormula
from hsp.hsp_variables import HSPVariables

if __name__ == '__main__':
   hsp = HarvestSchedulingProblem.make_from_input()
   print(hsp)
   
   variables = HSPVariables(hsp)
   print(variables)

   formula = HSPFormula(hsp, variables)
   print(formula)


# class Solver:
#     def __init__(self, variables:tuple[Variable]) -> None:
#         self.variables = variables
#         self.result = ()
#         self.cost = None

#     def solve(self, formula:WCNFPlus) -> None:
#         with RC2(formula, solver='gluecard4') as solver:
#             self.result = solver.compute()
#             self.cost = solver.cost
