from hsp import HarvestSchedulingProblem
from sat import Solver
from variables import hsp_variables
from clauses import hsp_clauses

if __name__ == '__main__':
   hsp = HarvestSchedulingProblem.make_from_input()
   # print(hsp)

   variables = hsp_variables(hsp)
   clauses = hsp_clauses(hsp)

   solver = Solver(variables, clauses)
   solver.solve() 

   for variable in variables:
      print(variable.result())