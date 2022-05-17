# Reasoning and Agents



## Week 1



##  Lecture 1 - Intelligent Agents and their Environments



#### Structure

![截屏2022-01-17 下午6.13.37](raa_notes.assets/截屏2022-01-17 下午6.13.37.png)

#### Agent

- Perceives its environment,
- Through its sensors,
- Then achieves its goals,
- By acting on its environment via actuators.



#### Categorise agents

- Environment
- Goals
- Percepts
- Actions



#### Example - Mail sorting

- Conveyor belt of letters
- Route letter into correct bin
- Array of pixel intensities
- Route letter into bin



#### Example - Autonomous car

![截屏2022-01-17 下午6.15.39](raa_notes.assets/截屏2022-01-17 下午6.15.39.png)

### Type of Intelligent Agents



#### Simple Reflex Agents

- Action depends only on immediate percepts.
- Implement by **condition-action rules**. 

- Example:
  - **Agent**: Mail sorting robot
  - **Environment**: Conveyor belt of letters
  - **Rule**: e.g. city=Edinburgh → put in Scotland bag

![截屏2022-01-17 下午6.19.17](raa_notes.assets/截屏2022-01-17 下午6.19.17.png)





#### Model-Based Reflex Agents

![截屏2022-01-17 下午6.20.48](raa_notes.assets/截屏2022-01-17 下午6.20.48.png)

![截屏2022-01-17 下午6.21.05](raa_notes.assets/截屏2022-01-17 下午6.21.05.png)





#### Goal-Based Agents

![截屏2022-01-17 下午6.21.27](raa_notes.assets/截屏2022-01-17 下午6.21.27.png)

![截屏2022-01-17 下午6.21.38](raa_notes.assets/截屏2022-01-17 下午6.21.38.png)



 #### Utility-Based Agents

- Agents so far have had a **single goal.** 
- Agents may have to juggle conflicting goals. 
- Need to optimise utility over a range of goals.



##### Utility:

measure of goodness (a real number). Combine with probability of success to get expected utility. 



##### Example

- Example: 
  - ◦ Agent: autonomous car. 
  - ◦ Environment: roads, vehicles, signs, etc. 
  - ◦ Goals: stay safe, reach destination, be quick, obey law, save fuel, etc.

![截屏2022-01-17 下午6.23.55](raa_notes.assets/截屏2022-01-17 下午6.23.55.png)





#### Learning Agents



#### How do agents improve their performance in the light of experience?

- Generate problems which will test performance.
- Perform activities according to rules, goals, model, utilities, etc
- Monitor performance and identify non-optimal activity
- Identify and implement improvements



### Types of Environments



#### Observable

- Fully
  - agent's sensors describe environment fully 
- Partially
  - some parts of the environment not visible; noisy sensors



#### Deterministic

- DETERMINISTIC
  - next state fully determined by current state and agent's actions

- STOCHASTIC
  - random changes - cannot be predicted exactly



**An environment may appear stochastic if it is only partially observable**



#### Sequential

- EPISODIC
  - next episode does not depend on previous actions
- SEQUENTIAL
  - actions affect the future



#### Static

- STATIC
  - environment unchanged while agent deliberates
- DYNAMIC
  - environment can change at any time or even continuously



#### Discrete

- DISCRETE
  - percepts, actions and episodes are discrete
- CONTINUOUS
  - continuous time flow



#### How many agents?

- SINGLE

- MULTI-AGENT

Consider how many object must be modelled as agents. Element of choice over which objects are considered agents	





## Lecture 2 - Problem Solving and Search



### Problem-solving Agents

![image-20220118154237257](raa_notes.assets/image-20220118154237257.png)

##### Example - Romania

On holiday in Romania; currently in Arad. 

Flight leaves tomorrow from Bucharest 

**Formulate goal:** 

- be in Bucharest 

**Formulate problem:** 

- states: various cities ◦ actions: drive between cities

**Find solution:** 

- sequence of cities, e.g., Arad, Sibiu, Fagaras, Buchare

![image-20220118154259293](raa_notes.assets/image-20220118154259293.png)



#### Problem types

- **Deterministic, fully observable** -> single-state problem
  - Agent knows exactly which state it will be in; solution is a sequence
- **Non-observable** -> sensorless problem (conformant problem)
  - Agent may have no idea where it is; solution is a sequence
- **Nondeterministic and/or partially observable** -> contingency problem
  - percepts provide new information about current state
  - often interleave search, execution
- **Unknown state space** -> exploration problem





##### Example : vacuum world





### Problem Formulation

![截屏2022-01-24 下午4.07.37](raa_notes.assets/截屏2022-01-24 下午4.07.37.png)







## Lecture 3



### Search strategies

- A search strategy is defined by picking the order of node expansion
  - ◦ Nodes are taken from the **frontier**.



#### Evaluating search strategies

 Time and space complexity are measured in terms of: 

- **b**: maximum branching factor of the search tree
- **d**: depth of the least-cost solution
- **m**: maximum depth of the state space (may be ∞)

![image-20220205152838971](raa_notes.assets/image-20220205152838971.png)



#### Recall: Tree Search

![image-20220205153008039](raa_notes.assets/image-20220205153008039.png)

![image-20220205153018259](raa_notes.assets/image-20220205153018259.png)



#### Repeated states

- Failure to detect repeated states can turn a **linear** problem into an **exponential** one!





#### Graph search

- Augment TREE-SEARCH with a new data-structure: 
  - the **explored set** (closed list), which remembers every expanded node
  - newly expanded nodes already in explored set are discarded



![image-20220205160908601](raa_notes.assets/image-20220205160908601.png)

	#### Breadth-first search

Expand shallowest unexpanded node

Implementation :

- frontier is a FIFO queue, i.e., new successors go at end



![image-20220205161019255](raa_notes.assets/image-20220205161019255.png)

![image-20220205161029583](raa_notes.assets/image-20220205161029583.png)

![image-20220205161119302](raa_notes.assets/image-20220205161119302.png)

![image-20220205161131837](raa_notes.assets/image-20220205161131837.png)

##### Algorithm

![image-20220205161151003](raa_notes.assets/image-20220205161151003.png



##### Properties of breath-first search

![image-20220205161225500](raa_notes.assets/image-20220205161225500.png)



##### Depth-first search

- Expand deepest unexpanded node
- Implementation :
  - frontier is a LIFO queue, i.e., new successors go at front



##### Properties of depth-first search

![image-20220205161334509](raa_notes.assets/image-20220205161334509.png)



#### Breath-first VS depth-first

- Breath-frst
  - When completeness is important.
  - When optimal solutions are important. 
- Depth-first
  - When solutions are dense and low-cost is important, especially space costs. 



### 





#### Depth-limited search

![截屏2022-01-24 下午5.40.52](raa_notes.assets/截屏2022-01-24 下午5.40.52.png)



#### Iterative deepening search

![image-20220205161542280](raa_notes.assets/image-20220205161542280.png)

![image-20220205161615247](raa_notes.assets/image-20220205161615247.png)



Number of nodes generated in an iterative deepening search to depth d with branching factor b: 


$$
N_{I D S}=(d) b+(d-1) b^{2}+\ldots+(2) b^{d-1}+(1) b^{d}
$$
Some cost associated with generating upper levels multiple times

Example: For b = 10, d = 5
$$
\begin{aligned}
&\mathrm{N}_{\mathrm{BFS}}=10+100+1,000+10,000+100,000=111,110 \\
&\mathrm{~N}_{\mathrm{IDS}}=50+400+3,000+20,000+100,000=123,450
\end{aligned}
$$


##### Properties of iterative deepening search

 

![image-20220205161808564](raa_notes.assets/image-20220205161808564.png)



#### Comparisons for all search algorithms

![image-20220205161841427](raa_notes.assets/image-20220205161841427.png)



## Lecture 4 - Informed Search



#### Best-first search

An instance of general TREE-SEARCH or GRAPH-SEARCH

- Use an evaluation function f(n) for each node n
  - estimate of "desirability"
- Expand most desirable unexpanded node, usually the node with the lowest evaluation





#### Heuristics / to find, to discover.

Any method that is believed or practically proven to be useful for the solution of a given problem.

- No guarantee that it will always work or lead to an optimal solution!

Use **heuristics** to **guide** tree search. 

- This may not change the worst case complexity of the algorithm, but can help in the average case.

We introduce conditions (admissibility, consistency) in order to identify good heuristics, i.e. those which actually lead to an improvement over uninformed search.



#### Greedy best-first search

- Evaluation function $f(n) = h(n)$ (heuristic)
  - **estimated cost** of cheapest path from state at node n to a goal state
  - e.g., $h_{SLD}(n) =$ straight-line distance from n to Bucharest



Greedy best-first search expands the node that **appears** to be closest to goal	



##### Properties of best-first search

![image-20220205162631404](raa_notes.assets/image-20220205162631404.png)



#### A* Search

- Evaluation function $f(n) = g(n) + h(n)$
  - $g(n) =$ cost so far to reach n
  - $h(n) =$ estimated cost from n to goal
  - $f(n) =$ estimated total cost of path through n to goal



Avoid expanding paths that are already expensive



### Heuristics



#### Admissible heuristics

- A heuristic h(n) is admissible if for every node n:

$$
h(n) \leq \boldsymbol{h}^{*}(\boldsymbol{n})
$$

where **h* (n)** is the true cost to reach the goal state from n.

An admissible heuristic never overestimates the cost to reach the goal, i.e., it is optimistic

Example: $h_{SLD}(n)$ (never overestimates the actual road distance)



#### Admissible heuristic = optimal A*

**h(n)** never overestimates the cost to reach the goal

Thus, $f(n) = g(n) + h(n)$ never overestimates the true cost of a solution



##### THEOREM

If h(n) is admissible, A* using `TREE-SEARCH` is optimal



##### Proof: Optimality of A*

Suppose some **suboptimal** goal G2 has been generated and is in the frontier. 

Let n be an unexpanded node in the frontier such that n is on a **shortest path** to an **optimal** goal G

![image-20220205163101091](raa_notes.assets/image-20220205163101091.png)



Hence $f(n) < f(G_2)$, and A* will never select G2 for expansion



#### Consistent heuristics

- A heuristic h(n) is consistent if for every node n, every successor n' of n generated by any action a,

$$
h(n) \leq c\left(n, a, n^{\prime}\right)+h\left(n^{\prime}\right)
$$

If h is consistent, we have
$$
\begin{aligned}
f\left(n^{\prime}\right) &=g\left(n^{\prime}\right)+h\left(n^{\prime}\right) \\
&=g(n)+c\left(n, a, n^{\prime}\right)+h\left(n^{\prime}\right) \\
& \geq g(n)+h(n) \\
& \geq f(n)
\end{aligned}
$$
i.e., f(n) is non-decreasing along any path.



##### THEOREM

If h(n) is consistent, A* using **GRAPH-SEARCH** is optimal



#### Optimality of A*

- A* expands nodes in order of increasing f value
- Gradually adds " fcontours" of nodes
- Contour i has all nodes with $f=_fi$ , where $f_i < f_i+1$



##### Properties of A*

![image-20220205163651325](raa_notes.assets/image-20220205163651325.png)



#### Admissible heuristics

Example: 8-puzzle:

- $h_1 (n) = $number of misplaced tiles
- $h_2 (n) = $total Manhattan distance



#### Dominance

![image-20220205163951251](raa_notes.assets/image-20220205163951251.png)



## Lecture 5 - Smart Search using Constraints



#### Structure of a CSP

- A set of **variables**: 

$$
X={X1
,… Xn
}
$$



-  A set of **domains**:
  - each domain Di is a set of possible values for variable Xi

$$
D={D1
,… Dn
}
$$



- A set of constraints C that specify acceptable combinations of values.
  - Each c ∈ C consists of:
    - a **scope** – tuple of variables (neighbours) involved in the constraint
    - a **relation** that defines the values that the variables can take



#### Example: Map-Colouring

Variables: {WA, NT, Q, NSW, V, SA, T}

Domains: Di = {red, green, blue}

Constraints: adjacent regions must have different colours,

- e.g. WA ≠ NT, 
- or (WA,NT) ∈ {(red, green), (red, blue), (green, red), (green, blue), (blue, red), (blue, green)}.



##### Example: Map-Colouring

Solutions are complete and consistent assignments

- e.g. WA = red, NT = green, Q = red, NSW = green, V = red, SA = blue, T = green.



![image-20220205172143530](raa_notes.assets/image-20220205172143530.png)

#### Constraint graph

##### Binary CSP: 

- each constraint relates two variables.

##### Constraint graph:

- nodes are variables, arcs are constraints



##### Varieties of CSPs

- **Discrete variables**:
  - finite domains:
    - n variables, domain size d → O(dn ), complete assignments
    - e.g. Boolean CSPs, incl. Boolean satisfiability (NP-complete).
  - infinite domains:
    - integers, strings, etc.
    - e.g. job scheduling, variables are start/end days for each job.
    - need a constraint language, e.g. StartJob1+ 5 ≤ StartJob3.



- **Continuous variables**:
  - e.g. start/end times for Hubble Space Telescope observations.
  - linear constraints solvable in polynomial time by linear programming.



#### Varieties of constraints

- Unary constraints involve a single variable, 
  - e.g. SA ≠ green.
- Binary constraints involve pairs of variables,
  - e.g. SA ≠ WA.
- Higher-order constraints involve 3 or more variables,
  - Higher-order constraints involve 3 or more variables,



Global constraints involve an arbitrary number of variables



#### Example: Crypt-arithmetic

![image-20220205172914457](raa_notes.assets/image-20220205172914457.png)

#### Real-world CSPs

![image-20220205172924374](raa_notes.assets/image-20220205172924374.png)



### Search in CSPs



#### Standard search formulation (incremental)







## Lecture 8 - Adversarial Search



#### Games vs. search problems

- "Unpredictable" opponent → solution is a strategy / policy
- Specify a move for every possible opponent reply

Time limits → unlikely to find goal, must approximate





#### Types of games

![截屏2022-02-07 下午2.47.11](raa_notes.assets/截屏2022-02-07 下午2.47.11.png)

#### Zero-sum games of perfect information

- Deterministic, fully observable

- Agents act alternately
- Utilities at end of game are equal and opposite (adding up to 0)



#### Game tree (2 -player, deterministic, turns)

- 2 players: MAX and MIN 
- MAX moves first

- Tree built from MAX’s POV
- ![截屏2022-02-07 下午2.49.05](raa_notes.assets/截屏2022-02-07 下午2.49.05.png)

#### Optimal Decisions

- Normal search: 
  - optimal decision is a sequence of actions leading to a goal state (i.e. a winning terminal state)
- Adversarial search: 
  - MIN has a say in game
  - MAX needs to find a contingent strategy which specifies:
  - MAX’s move in initial state then…
  - MAX’s moves in states resulting from every response by MIN to the move then…
  - MAX’s moves in states resulting from every response by MIN to all those moves, etc…



#### Minimax value

minimax value of a node = utility for MAX of being in corresponding state:
$$
\operatorname{Minimax}(s)= \begin{cases}\text { Utility(s) } & \text { if Terminal-Test(s) } \\ \max _{a \in A c t i o n s(s)} \operatorname{Minimax}(Result(s, a)) & \text { if Players(s) }=M A X \\ \min _{a \in A c t i o n s(s)} \operatorname{Minimax}(Result(s, a)) & \text { if Players(s) }=M I N\end{cases}
$$

#### Minimax

- Perfect play for deterministic, perfect - information games
- Idea: choose move to position with highest minimax value
- = best achievable payoff against best play



![截屏2022-02-07 下午2.54.23](raa_notes.assets/截屏2022-02-07 下午2.54.23.png)

##### Minimax algorithm

![截屏2022-02-07 下午2.56.27](raa_notes.assets/截屏2022-02-07 下午2.56.27.png)

##### Properties of Minimax

![截屏2022-02-07 下午2.57.12](raa_notes.assets/截屏2022-02-07 下午2.57.12.png)





### α-β pruning



#### α-β pruning example

Let pruned leaves have values u and v
$$
\begin{aligned}
\operatorname{MINIMAX}(\operatorname{root}) &=\max (\min (3,12,8), \min (2, u, v), \min (14,5,2)) \\
&=\max (3, \min (2, u, v), 2) \\
&=\max (3, z, 2) \quad \text { where } z \leq 2 \\
&=3
\end{aligned}
$$


![截屏2022-02-07 下午3.30.35](raa_notes.assets/截屏2022-02-07 下午3.30.35.png)

#### Why is it called α-β?

α is the value of the best (i.e., highest-value) choice found so far at any choice point along the path for MAX

If v is worse than α, MAX will avoid it

- prune that branch

β is defined symmetrically for MIN





#### The α - β algorithm 

- α is value of the best i.e. highest -value choice found so far at any choice point along the path for MAX
- β is value of the best i.e. lowest -value choice found so far at any choice point along the path for MIN

![截屏2022-02-07 下午3.33.52](raa_notes.assets/截屏2022-02-07 下午3.33.52.png)

#### Complexity of α-β

- Pruning does not affect final result (as we saw for example)
- Good move ordering improves effectiveness of pruning
- With “perfect ordering”, time complexity = $O(b^{m/2}$)
  - branching factor goes from 𝑏 to 𝑏
  - doubles solvable depth of search compared to minimax
- A simple example of the value of reasoning about which computations are relevant (a form of meta-reasoning)



#### Resource limits

Minimax tries to find the best possible move from all 10^6 nodes, can only look 4 steps ahead.

Need to fine-tune the algorihym to find the most intersting path





#### Standard approach to improve algorithm



## Lecture 10 - Effective Propositional Inference



#### Conversion to CNF

![image-20220214143030812](raa_notes.assets/image-20220214143030812.png)



#### Unit clause heuristic



##### Unit clause: 
 - only one literal in the clause



### The DPLL algorithm



#### Pure symbol:

- always appears with the same “sign” or polarity in all clauses.
- e.g., In the three clauses $(A \vee \neg B),(\neg B \vee \neg C),(C \vee A)$:
- A and B are pure, C is impure. 



#### Tautology:

- both a proposition and its negation in a clause.
- e.g. (A, B, ¬A)



#### Lecture 11 - First order logic



## Lecture 17



#### Forward state-space search

- Formulation of planning problem: 
  - Initial state of search is initial state of planning problem (=set of positive literals) Applicable actions are those whose preconditions are satisfied Single successor function works for all planning problems (consequence of action representation) Goal test = checking whether state satisfies goal of planning problem Step cost usually 1, but different costs can be allowed


$$
n \times(n+n) \\
= n (2n) \\
= n^2 = O(n^2)
$$
