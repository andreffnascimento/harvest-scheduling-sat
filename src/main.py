from hsp import HarvestSchedulingProblem
from variables import hsp_variables

if __name__ == '__main__':
   hsp = HarvestSchedulingProblem.make_from_input()
   print(hsp)

   variables = hsp_variables(hsp)
   for variable in variables:
      print(variable)