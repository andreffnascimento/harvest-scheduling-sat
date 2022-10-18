from sat.variables import Variable

from hsp.hsp import HarvestSchedulingProblem


class HSPVariables:
    def __init__(self, hsp:HarvestSchedulingProblem) -> None:
        self.hsp = hsp
        self.adj  = ()
        self.harv = ()
        self.nat  = ()
        self.aux = ()
        self.conn_pred = ()
        self.conn_depth = ()
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

    def __len__(self):
        return len(self.__variables)

    def true_vars(self) -> str:
        hsp_variables_str = ('=' * 80) + '\n\tTrue Variables\n' + ('=' * 80) + '\n'
        for variable in self.__variables:
            if variable.value:
                hsp_variables_str += str(variable) + '\n'
        return hsp_variables_str

    def add_new_aux_variables(self, variable_ids:tuple[int]):
        for variable_id in variable_ids:
           if variable_id > len(self.__variables):
                self.aux += (self.__create_variable('Aux[' + str(len(self.aux) + 1) + ']'),)

    def set_result(self, result:tuple[int]|None) -> None:
        if result == None:
            return
        for i in range(len(result)):
            self.__variables[i].value = (result[i] > 0)

    def __create_variable(self, description) -> Variable:
        variable = Variable(description)
        self.__variables += (variable,)
        return variable

    def __create_variables(self) -> None:
        self.__create_adj_variables()
        self.__create_harv_variables()
        self.__create_nat_variables()
        self.__create_conn_pred_variables()
        self.__create_conn_depth_variables()

    def __create_adj_variables(self) -> None:
        for area1 in self.hsp.areas:
            adj_variables = ()
            for area2 in self.hsp.areas:
                adj_variables  += (self.__create_variable('Adj[' + str(area1) + ',' + str(area2) + ']'),)
            self.adj += (adj_variables,)

    def __create_harv_variables(self) -> None:
        for area in self.hsp.areas:
            harv_variables = ()
            for t in range(self.hsp.n_periods):
                harv_variables += (self.__create_variable('Harv[' + str(area) + ',' + str(t + 1) + ']'),)
            self.harv += (harv_variables,)

    def __create_nat_variables(self) -> None:
        for area in self.hsp.areas:
            self.nat += (self.__create_variable('Nat[' + str(area) + ']'),)

    def __create_conn_pred_variables(self) -> None:
        for i in range(0, self.hsp.n_areas + 1):
            conn_pred_variables  = ()
            for j in range(0, self.hsp.n_areas + 1):
                conn_pred_variables  += (self.__create_variable('Conn_Pred['  + str(i) + ',' + str(j) + ']'),)
            self.conn_pred  += (conn_pred_variables,)

    def __create_conn_depth_variables(self) -> None:
        for i in range(0, self.hsp.n_areas + 1):
            conn_depth_variables = ()
            for j in range(0, self.hsp.n_areas + 3):
                conn_depth_variables += (self.__create_variable('Conn_Depth[' + str(i) + ',' + str(j) + ']'),)
            self.conn_depth += (conn_depth_variables,)
