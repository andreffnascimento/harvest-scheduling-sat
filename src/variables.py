from sat import Variable
from hsp import HarvestSchedulingProblem



def adjacency_variables(hsp:HarvestSchedulingProblem) -> tuple[Variable]:
    variables = ()
    for area1 in hsp.areas:
        for area2 in hsp.areas:
            variables += (Variable('Adj[' + str(area1) + ',' + str(area2) + ']', area2 in area1.adjacencies),)
    return variables


def harvest_variables(hsp:HarvestSchedulingProblem) -> tuple[Variable]:
    variables = ()
    for area in hsp.areas:
        for period in range(hsp.n_periods):
            variables += (Variable('Harv[' + str(area) + ',' + str(period + 1) + ']'),)
    return variables


def nature_reserve_variables(hsp:HarvestSchedulingProblem) -> tuple[Variable]:
    variables = ()
    for area in hsp.areas:
        variables += (Variable('Nat[' + str(area) + ']'),)
    return variables


def connected_nature_reserve_variables(hsp:HarvestSchedulingProblem) -> tuple[Variable]:
    variables = ()
    for area1 in hsp.areas:
        for area2 in hsp.areas:
            variables += (Variable('Conn[' + str(area1) + ',' + str(area2) + ']'),)
    return variables


def hsp_variables(hsp:HarvestSchedulingProblem) -> tuple[Variable]:
    variables = ()
    variables += adjacency_variables(hsp)
    variables += harvest_variables(hsp)
    variables += nature_reserve_variables(hsp)
    variables += connected_nature_reserve_variables(hsp)
    return variables