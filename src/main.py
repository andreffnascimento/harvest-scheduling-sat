from hsp import HarvestSchedulingProblem
from sat import Solver
from variables import hsp_variables

if __name__ == '__main__':
   hsp = HarvestSchedulingProblem.make_from_input()
   print(hsp)

   variables = hsp_variables(hsp)

   solver = Solver(variables)
   solver.solve() 