# Variables

## Sets of Variables
$U \rightarrow \text{Units}$        \
$T \rightarrow \text{Periods}$

<br>

## Input Variables:
$A_{i} \rightarrow \text{size of the unit }i \in U$                                             \
$Prof_{it} \rightarrow \text{profit of unit }i \in U \text{ in the period }t \in T$

<br>

## Logical Variables:

$Adj_{ij} \rightarrow \text{true if unit }i \in U\text{ is adjacent to unit } j \in U$          \
$Harv_{it} \rightarrow \text{true if unit }i \in U\text{ was harvested in period } t \in T$     \
$Nat_{i} \rightarrow \text{true if }i \in U\text{ is a nature reserve}$

<br>
<br>



# Hard Clauses:

$\text{Each unit can only be harvest at most once in T periods:}$
$\forall_{i \in U} \sum_{t \in T} Harv_{it} \le 1$

$\text{Two adjacent units cannot be harvested at the same time:}$
$\forall_{i,j \in U} Adj_{ij} \implies (\neg Harv_{it} \lor \neg Harv_{jt}), t \in T$

$\text{Natural reserves cannot be harvested:}$
$\forall_{i \in U} Nat_{i} \implies \forall_{t \in T} \neg Harv_{it}$

$\text{The total size of the natural reserve must be at least the minimum:}$
$\sum_{i \in U} A_{i} \cdot Nat_{i} \ge A_{min}$

<br>
<br>



# Soft Clauses:

$\text{Maximize the harvest profit:}$
$max \sum_{i \in U, t \in T} Prof_{it} \cdot Harv_{it}$

<br>
<br>



# Connected Natural Reserve Clauses:

**Units with root** $\rightarrow U' = U \cup \{0\}$     \
**Possible depths** $\rightarrow D = \{0, ..., (\#U + 1)\}$

<br>

## New Variables

$Pred_{ij} \rightarrow \text{true if unit }i \in U' \text{ is the predecessor of unit }j \in U'$

$Depth_{id} \rightarrow \text{true if unit }i \in U' \text{ has a depth of }d \in U' \cup \{\#U + 1\}$

## Constraints
$\text{Each unit has a unique depth:}$
$\forall_{i \in U} \sum_{d \in D} Depth_{id} \le 1$

$\text{Each unit has a single predecessor:}$
$\forall_{i \in U} \sum_{j \in U} Pred_{ij} \le 1$

$\text{The root can only be the predecessor of a single unit:}$
$\sum_{j \in U} Pred_{0j} \le 1$

$\text{The depth of the root is one:}$
$Depth_{01}$

$\text{Units that aren't nature reserves always have a depth of 0:}$
$\forall_{i \in U} \neg Nat_{i} \implies Depth_{i0}$

$\text{Nature reserves cannot have the depth one:}$
$\forall_{i \in U} Nat_{i} \implies \neg Depth_{i1}$

$\text{Nature reserves must always have a predecessor (unit or root):}$
$\forall_{i \in U} Nat_{i} \implies \bigvee_{j \in U'} Pred_{ji}$

$\text{If a unit is a precessor of another, than they must be adjacent:}$
$\forall_{i,j \in U} Pred_{ij} => Adj_{ij}$

$\text{If the depth of a predecessor is d, than the depth of the preceded is d+1:}$
$\forall_{i,j \in U'} Pred_{ij} \land Depth_{jd} \implies Depth_{i(d+1)}$
