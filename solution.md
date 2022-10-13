# Variables

## Sets of Variables
$U \rightarrow \text{Units}$        \
$T \rightarrow \text{Periods}$

<br>

## Input Variables:
$A_{i} \rightarrow \text{size of the unit }i \in U$

<br>

## Logical Variables:

$Adj_{ij} \rightarrow \text{true if unit }i \in U\text{ is adjacent to unit } j \in U$          \
$Harv_{it} \rightarrow \text{true if unit }i \in U\text{ was harvested in period } t \in T$     \
$Nat_{i} \rightarrow \text{true if }i \in U\text{ is a nature reserve}$                         \
$Conn_{ij} \rightarrow \text{true if the both units }i \in U\text{ and } j \in U \text{ are nature reserves and indirectly connected}$

<br>
<br>



# Hard Constrains:

## Generic

$\text{Each unit can only be harvest at most once in T periods:}$
$\forall_{i \in U} \sum_{t \in T} Harv_{it} \le 1$

$\text{Two adjacent units cannot be harvested at the same time:}$
$\forall_{i,j \in U} Adj_{ij} \implies (\neg Harv_{it} \lor \neg Harv_{jt}), t \in T$

$\text{Natural reserves cannot be harvested:}$
$\forall_{i \in U} Nat_{i} \implies \forall_{t \in T} \neg Harv_{it}$

$\text{The total size of the natural reserve must be at least the minimum:}$
$\sum_{i \in U} A_{i} \cdot Nat_{i} \ge A_{min}$

<br>

## Connected Nature Reserve
$\text{The units that are part of the nature reserve must be connected:}$
$$\forall_{i,j \in U} (\neg N_{i} \lor \neg N_{j}) \implies \neg Conn_{ij}$$
$$\forall_{i,j \in U} (N_{i} \land N_{j} \land Adj_{ij}) \implies Conn_{ij}$$
$$\forall_{i,j,k \in U} (Conn_{ik} \land Conn_{kj}) \implies Conn_{ij}$$
$$\forall_{i,j \in U} (N_{i} \land N_{j}) \implies Conn_{ij}$$