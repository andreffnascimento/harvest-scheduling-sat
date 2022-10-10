from hsp import HarvestSchedulingProblem
from sat import Solver
from variables import hsp_variables
from formula import hsp_formula

if __name__ == '__main__':
   hsp = HarvestSchedulingProblem.make_from_input()

   variables = hsp_variables(hsp)
   formula = hsp_formula(hsp, variables)

   solver = Solver(variables)
   solver.solve(formula) 

   # for variable in variables:
   #    print(variable.result())