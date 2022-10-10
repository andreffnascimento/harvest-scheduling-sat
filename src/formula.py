from hsp import HarvestSchedulingProblem
from pysat.formula import WCNFPlus
from pysat.pb import PBEnc

def harvest_at_most_once_clauses(hsp:HarvestSchedulingProblem, variables:dict, formula:WCNFPlus) -> None:
    harv_variables = variables['Harv']
    for i in range(hsp.n_areas):
        variable_ids = [harv_variables[i][t].id for t in range(hsp.n_periods)]
        formula.append([variable_ids, 1], is_atmost=True)

def adjacent_harvest_same_time_clauses(hsp:HarvestSchedulingProblem, variables:dict, formula:WCNFPlus) -> None:
    adj_variables  = variables['Adj']
    harv_variables = variables['Harv']
    for i in range(hsp.n_areas):
        for j in range(hsp.n_areas):
            for t in range(hsp.n_periods):
                adj_ij  = adj_variables[i][j].id
                harv_it = harv_variables[i][t].id
                harv_jt = harv_variables[j][t].id
                formula.append([-adj_ij, -harv_it, -harv_jt])
    print(formula.hard)
    print(formula.soft)
    print(formula.atms)

def minimum_natural_reserve_size(hsp:HarvestSchedulingProblem, variables:dict, formula:WCNFPlus) -> None:
    nat_variables = variables['Nat']
    variables = [nat_variables[i].id for i in range(hsp.n_areas)]
    weights = [area.size for area in hsp.areas]
    PBEnc.atleast(variables, weights, hsp.min_natural_reserve).clauses
    for clause in PBEnc.atleast(variables, weights, hsp.min_natural_reserve).clauses:
        formula.append(clause)


def hsp_formula(hsp:HarvestSchedulingProblem, variables:dict) -> WCNFPlus:
    formula = WCNFPlus()
    harvest_at_most_once_clauses(hsp, variables, formula)
    adjacent_harvest_same_time_clauses(hsp, variables, formula)
    minimum_natural_reserve_size(hsp, variables, formula)
    return formula