# CS50's Introduction to Artificial Intelligence with Python

## 0. Search

Example problems

* 15 number puzzle (sort in order)
* Maze
* Driving directions

### Terminology: Search Problems

* **Agent**: entity that perceives its environment and acts upon that environment
* **State**: a configuration of the agent and its environment
* **Initial state**: the state in which the agent begins
* **Actions**: choices that can be made in a state (or a function taking a state as an argument and returning a set of actions which can be executed in that state)
* **Transition model**: a description of what state results from performing any applicable action in any state (`result(state, action) -> state`)
* **State space**: the set of all states reachable from the initial state by any sequence of actions
* **Goal test**: way to determine whether a given state is a goal state
* **Path cost**: numerical cost associated with a given path
* **Optimal solution**: a solution that has the lowest path cost among all solutions

Data structures:

* **Node**: state + parent + action (from parent to node) + path cost (total to get to this node)
* **Frontier**: nodes of current interest, stack or queue
* **"Expanding a node"**: looking a all the next nodes that follow a node
* **Explored set**: nodes already evaluated

Depth-first search (stack frontier), breadth-first search (queue frontier)

### Types of search algorithms

* **Uninformed search**: search strategy that uses no problem-specific knowledge
* **Informed search**: search strategy that uses problem-specific knowledge to find solutions more efficiently

* **Greedy best-first search**: search algorithm that expands the node that is closest to the goal, as estimated by a heuristic function `h(n)`
* **Manhattan distance**
* **A star search**: expands node with lowest value of `g(n) + h(n)` (g ... cost to reach node, h ... estimated cost to goal)

A star is optimal if:
- h(n) is admissible (never overestimates the true cost)
- h(n) is consistent (for every node `n` and successor `n'` with step cost `c`: `h(n) <= h(n') + c`)

* **Adversarial search**:
* **Minimax algorithm**: Max player aims to maximize score, min player tries to minimize score
* **Alpha-beta pruning**: Minimax optimization
* **Depth-limited minimax**: limited number of lookahead
* **Evaluation function**: function that estimates the expected utility of the game from a given state

## 1. Knowledge
