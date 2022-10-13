from sat.variables import Variable, VariableGenerator

from hsp.hsp import HarvestSchedulingProblem


class HSPVariables:
    def __init__(self, hsp:HarvestSchedulingProblem) -> None:
        self.hsp = hsp
        self.adj  = ()
        self.harv = ()
        self.nat  = ()
        self.conn = ()
        self.__variables = ()
        self.__create_variables()
    
    def __str__(self) -> str:
        hsp_variables_str = ('=' * 80) + '\n\tVariables\n' + ('=' * 80) + '\n'
        for variable in self.__variables:
            hsp_variables_str += str(variable) + '\n'
        return hsp_variables_str

    def __repr__(self) -> str:
        return str(self.adj + self.harv + self.nat + self.conn)

    def __getitem__(self, id:int) -> Variable:
        return self.__variables[id - 1]

    def __create_variable(self, description) -> Variable:
        variable = Variable(description)
        self.__variables += (variable,)
        return variable

    def __create_variables(self) -> None:
        for area1 in self.hsp.areas:
            adj_variables = ()
            harv_variables = ()
            conn_variables = ()
            for area2 in self.hsp.areas:
                adj_variables  += (self.__create_variable('Adj[' + str(area1) + ',' + str(area2) + ']'),)
                conn_variables += (self.__create_variable('Conn[' + str(area1) + ',' + str(area2) + ']'),)
            for t in range(self.hsp.n_periods):
                harv_variables += (self.__create_variable('Harv[' + str(area1) + ',' + str(t + 1) + ']'),)
            self.adj  += (adj_variables,)
            self.conn += (conn_variables,)
            self.harv += (harv_variables,)
            self.nat  += (self.__create_variable('Nat[' + str(area1) + ']'),)
