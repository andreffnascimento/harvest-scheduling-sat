from hsp import HarvestSchedulingProblem
from sat import Clause, HardClause


def harvest_at_most_once_clauses(hsp:HarvestSchedulingProblem) -> tuple[HardClause]:
    return ()

def adjacent_harvest_same_time_clauses(hsp:HarvestSchedulingProblem) -> tuple[HardClause]:
    return ()

def minimum_natural_reserve_size(hsp:HarvestSchedulingProblem) -> tuple[HardClause]:
    return ()


def hsp_clauses(hsp:HarvestSchedulingProblem) -> tuple[Clause]:
    clauses = ()
    clauses += harvest_at_most_once_clauses(hsp)
    clauses += adjacent_harvest_same_time_clauses(hsp)
    clauses += minimum_natural_reserve_size(hsp)
    return clauses