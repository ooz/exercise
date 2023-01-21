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

* **Sentence**: an assertion about the world in a knowledge representation language
* Propositional logic, propositional symbols
* **Model**: assignment of a truth value to every propositional symbol (a "possible world")
* **Knowledge base**: a set of sentences known by a knowledge-based agent
* Entailment
* **Inference**: the process of deriving new sentences from old ones
* **Inference algorithms**: does a knowledge base entail a sentence?

### Model Checking

* Enumerate all possible models and check for which the query is true

### Inference rules

* Modus Ponens
* And Elimination
* Double Negation Elimination
* Implication Elimination
* Biconditional Elimination
* De Morgan's Law
* Distributive Property
* Inference by resolution
* Factoring

### Theorem Proving as a search problem

* Initial state: starting knowledge base
* Actions: inference rules
* Transition model: new knowledge base after inference
* Goal test: check statement we're trying to prove
* Path cost function: number of steps in proof

### Normal forms

* **Clause**: a disjunction (or-chain) of literals
* **Conjunctive normal form (CNF)**: logical sentence that is a conjunction (and-chain) of clauses
    - Eliminate biconditionals
    - Eliminate implications
    - Move not inwards (De Morgan's Laws)
    - Use distributive law

### Inference by Resolution

* To determine if KB entails statement: Check if (KB and not statement) is a contradiction (by trying to produce the empty clause ("false"))
    - If so, then KB entails statement
    - Otherwise, no entailment

### First-Order Logic

* Constant symbol, predicate symbol (functions)
* Universal quantification ("all")
* Existential quantification ("exists")

## 2. Uncertainty

### Probability

* Possible worlds *w*
* Probability of possible world: 0 <= *P(w)* <= 1
* The sum of all probabilities of all possible worlds is 1
* Unconditional, conditional probability: *P(a|b) = P(a and b) / P(b)*, *P(a and b) = P(b)P(a|b)*, *P(a and b) = P(a)P(b|a)*
* Random variable, domain of values (e.g. dice roll: 1, 2, 3, 4, 5, 6)
* Probability distribution
* Independence: *P(a and b) = P(a)P(b)*

Bayes' Rule: *P(b|a) = (P(a|b)P(b)) / P(a)*

Knowing *P(visible effect | unknown cause)* we can calculate *P(unknown cause | visible effect)* using Bayes' Rule!

* Joint probability, joint probability distribution
* Conditional distribution is proportional to the joint probability
* Negation: *P(not a) = 1 - P(a)*
* Inclusion-Exclusion: *P(a or b) = P(a) + P(b) - P(a and b)*
* Marginalization: *P(a) = P(a, b) + P(a, not b)* (*P(a, b)* is alternative notation for *P(a and b)*)
* Conditioning: *P(a) = P(a|b)P(b) + P(a|not b)P(not b)*

* **Bayesian network**: data structure that represents the dependencies among random variables.
  It is a directed graph, each node represents a random variable. Arrow from *X* to *Y* means *X* is a parent of *Y*.
  Each node *X* has a probability distribution *P(X | Parents(X))*

### Inference

* Query *X*: variable for which to compute distribution
* Evidence variables *E*: observed variables for event *e*
* Hidden variables *Y*: non-evidence, non-query variable
* Goal: calculate *P(X|e)*, calculate it with **inference by enumeration**
* `pomegranate` library to model Bayesian networks
* Approximate inference, sampling, likelihood weighting

### Uncertainty over Time

* **Markov assumption**: the current state depends on only a finite fixed number of previous states
* **Markov chain**: sequence of random variables where the distribution of each variable follows the Markov assumption
* **Hidden Markov model** or **sensor model**: Markov model for a system with hidden states that generate some observed event
* **Sensor Markov assumption**: the evidence variable depends only on the corresponding state

Possible tasks:

|Task|Definition|
|---|---|
|**filtering**|given observations from start until now, calculate distribution for current state|
|**prediction**|given observations from start until now, calculate distribution for a future state|
|**smoothing**|given observations from start until now, calculate distribution for past state|
|**most likely explanation**|given observations from start until now, calculate most likely sequence of states|


