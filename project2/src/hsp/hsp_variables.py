from z3 import Int, Bool

from hsp.hsp import HarvestSchedulingProblem


class HSPVariables:
    def __init__(self, hsp:HarvestSchedulingProblem) -> None:
        self.hsp = hsp
        self.harv = ()
        self.prof = ()
        self.nat = ()
        self.natsize = ()
        self.root = None
        self.__create_variables()

    def __str__(self) -> str:
        hsp_variables = ('=' * 80) + '\n\tVariables\n' + ('=' * 80) + '\n'
        for var in self.get_variables():
            hsp_variables += f'{str(var)}\n'
        return hsp_variables

    def __repr__(self) -> str:
        return str(self.get_variables())

    def get_variables(self) -> tuple:
        return self.harv + self.prof + self.nat + self.natsize + (self.root,)

    def __create_variables(self) -> None:
        for area in self.hsp.areas:
            self.harv    += (Int(f'Harv_{area.id}'),)
            self.prof    += (Int(f'Prof_{area.id}'),)
            self.nat     += (Int(f'Nat_{area.id}'),)
            self.natsize += (Int(f'NatSize_{area.id}'),)
            self.root     =  Int(f'Root')