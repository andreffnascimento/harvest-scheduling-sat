from hsp import HarvestSchedulingProblem
from sat import Variable


def adjacency_variables(hsp:HarvestSchedulingProblem) -> tuple[tuple[Variable]]:
    variables = ()
    for area1 in hsp.areas:
        variables_area1 = ()
        for area2 in hsp.areas:
            variables_area1 += (Variable('Adj[' + str(area1) + ',' + str(area2) + ']', area2 in area1.adjacencies),)
        variables += (variables_area1,)
    return variables

def harvest_variables(hsp:HarvestSchedulingProblem) -> tuple[Variable]:
    variables = ()
    for area in hsp.areas:
        variables_area = ()
        for period in range(hsp.n_periods):
            variables_area += (Variable('Harv[' + str(area) + ',' + str(period + 1) + ']'),)
        variables += (variables_area,)
    return variables

def nature_reserve_variables(hsp:HarvestSchedulingProblem) -> tuple[Variable]:
    variables = ()
    for area in hsp.areas:
        variables += (Variable('Nat[' + str(area) + ']'),)
    return variables

def connected_nature_reserve_variables(hsp:HarvestSchedulingProblem) -> tuple[Variable]:
    variables = ()
    for area1 in hsp.areas:
        variables_area1 = ()
        for area2 in hsp.areas:
            variables_area1 += (Variable('Conn[' + str(area1) + ',' + str(area2) + ']'),)
        variables += variables_area1
    return variables


def hsp_variables(hsp:HarvestSchedulingProblem) -> dict:
    variables = {}
    variables['Adj']  = adjacency_variables(hsp)
    variables['Harv'] = harvest_variables(hsp)
    variables['Nat']  = nature_reserve_variables(hsp)
    variables['Conn'] = connected_nature_reserve_variables(hsp)
    return variables