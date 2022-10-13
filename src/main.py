from hsp.hsp import HarvestSchedulingProblem
from hsp.hsp_formula import HSPFormula
from hsp.hsp_output import HSPOutput
from hsp.hsp_variables import HSPVariables
from sat.solver import Solver

if __name__ == '__main__':
   hsp = HarvestSchedulingProblem.make_from_input()
   print(hsp)
   
   variables = HSPVariables(hsp)
   formula = HSPFormula(hsp, variables)
   print(formula)

   solver = Solver(formula.formula)
   print('Solving...')

   variables.set_result(solver.solve())
   print(variables)
   print('Cost = ' + str(solver.cost) + '\n\nOutput:')

   hsp_output = HSPOutput(hsp, variables, solver.cost)
   print(hsp_output)