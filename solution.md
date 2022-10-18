# Variables

## Sets of Variables
$U \rightarrow \text{Units}$                                                                    \
$T \rightarrow \text{Periods}$                                                                  \
$D \rightarrow \text{Possible depth in the nature reserve tree} = \large{[0, \frac{n}{2}]}$ \
$Adj(i) \rightarrow \text{Variables adjacent to unit i}$

<br>

## Input Variables:
$A_{i} \rightarrow \text{size of the unit }i \in U$                                             \
$Prof_{it} \rightarrow \text{profit of unit }i \in U \text{ in the period }t \in T$

<br>

## Logical Variables:

$Adj_{ij} \rightarrow \text{true if unit }i \in U\text{ is adjacent to unit } j \in U$          \
$Harv_{it} \rightarrow \text{true if unit }i \in U\text{ was harvested in period } t \in T$     \
$Nat_{i} \rightarrow \text{true if }i \in U\text{ is a nature reserve}$                         \
$Depth_{id} \rightarrow \text{true if the depth of the nature reserve }i \in U\text{ is }d \in D$

**Maximum Depth in the Nature Reserve Tree** $\rightarrow \large{\frac{n + 1}{2}}$


<br>
<br>



# Problem Clauses:

## Hard Clauses:

$\text{Each unit can only be harvest at most once in T periods}$                                \
$\forall i \in U , \sum \limits_{t \in T} Harv_{i,t} \le 1$

$\text{Two adjacent units cannot be harvested at the same time}$                                \
$\forall i,j \in U , Adj_{i,j} \implies (\neg Harv_{i,t} \lor \neg Harv_{j,t}), t \in T$

$\text{Natural reserves cannot be harvested}$                                                   \
$\forall i \in U , Nat_{i} \implies (\bigwedge\limits_{t \in T} \neg Harv_{i,t})$

$\text{The total size of the natural reserve must be at least the minimum}$                     \
$\sum \limits_{i \in U} A_{i} \cdot Nat_{i} \ge A_{min}$

<br>
<br>

## Soft Clauses (Optimization):

$\text{Maximize the harvest profit}$                                                            \
$\forall i \in U , \forall t \in T , Prof_{it} \cdot Harv_{it}$

<br>
<br>

## Connected Natural Reserve Clauses:

$\text{All units that are not nature reserves do not have any depth}$                           \
$\forall i \in U , \neg Nat_{i} \implies (\bigwedge \limits_{d \in D} \neg Depth_{i,d})$

$\text{All nature reserve units must have a single depth}$                                      \
$\forall i \in U , Nat_{i} \implies (\sum \limits_{d \in D} Depth_{i,d} = 1)$

$\text{At most one node has the depth 0}$                                                       \
$\sum \limits_{i \in U} Depth_{i,0} \le 1$

$\text{Every nature reserve of depth i must be adjacent to a nature reserve of depth i-1:}$     \
$\forall i \in U , \forall d \in D\setminus\{0\} , Depth_{i,d} \implies (\bigvee \limits_{j \in Adj(i)} Depth_{j,d-1})$