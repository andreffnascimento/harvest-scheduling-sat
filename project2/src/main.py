from z3 import sat

from hsp.hsp import HarvestSchedulingProblem
from hsp.hsp_formula import HSPFormula
from hsp.hsp_output import HSPOutput
from hsp.hsp_variables import HSPVariables


__debug = True

def __debug_log(argument) -> None:
   if __debug:
      print(argument)



if __name__ == '__main__':
   hsp = HarvestSchedulingProblem.make_from_input()
   __debug_log(hsp)
   
   variables = HSPVariables(hsp)
   formula = HSPFormula(hsp, variables)
   __debug_log(formula.get_solver())

   solver = formula.get_solver()
   if solver.check() == sat:
      model = solver.model()
      hsp_output = HSPOutput(hsp, variables, model)
      __debug_log(hsp_output.variable_values())
      __debug_log("\n")
      print(hsp_output)
   else:
      print('The problem instance is unsatisfiable')