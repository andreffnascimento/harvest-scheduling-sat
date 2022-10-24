from hsp.hsp import HarvestSchedulingProblem
from hsp.hsp_formula import HSPFormula
from hsp.hsp_output import HSPOutput
from hsp.hsp_variables import HSPVariables
from sat.solver import Solver

__debug = False

def __debug_log(argument):
   if __debug:
      print(argument)



if __name__ == '__main__':
   hsp = HarvestSchedulingProblem.make_from_input()
   __debug_log(hsp)
   
   variables = HSPVariables(hsp)
   formula = HSPFormula(hsp, variables)
   __debug_log(formula)

   solver = Solver(formula.formula)
   __debug_log('Solving...')

   variables.set_result(solver.solve())
   __debug_log(variables)
   __debug_log(variables.true_vars())

   hsp_output = HSPOutput(hsp, variables, solver.cost)
   print(hsp_output)
