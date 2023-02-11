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

## 3. Optimization

... choosing the best option from a set of options.

* **Local search**: search algorithms that maintain a single node and search by moving to a neighboring node
* State-space landscape, global maximum (objective function), global minimum (cost function)
* **Hill climbing**, local maxima/minima, flat local maximum, shoulder

Hill climbing variants:

|Variant|Definition|
|---|---|
|steepest-ascent|choose the highest-valued neighbor|
|stochastic|choose randomly from higher-valued neighbors|
|first-choice|choose the first higher-valued neighbor|
|random-restart|conduct hill climbing multiple times|
|local beam search|chooses the *k* highest-valued neighbors|

### Simulated Annealing

* Early on, higher "temperature": more likely to accept neighbors that are worse than current state
* Later on, lower "temperature": less likely to accept neighbors that are worse than current state

### Traveling Salesman Problem

NP complete problem

### Linear Programming

* Minimize a cost function (or maximize an objective function)
* With constraints
* With bounds for each variable

Algorithms: Simplex, Interior-Point (use `scipy.linprog`)

### Constraint Satisfaction

* Constraint graph
* Constraint satisfaction problem: variables, domains, constraints (hard, soft)
* Unary constraint (between variable and domain), binary constraint (between variables)
* **Node consistency**: when all the values in a variable's domain satisfy the variable's unary constraints
* **Arc consistency**: when all the values in a variable's domain satisfy the variable's binary constraints
* To make *X* arc-consistent with respect to *Y*, remove elements from *X*'s domain until every choice for *X* has a possible choice for *Y*
* AC-3 algorithm makes a constraint satisfaction problem (CSP) arc-consistent
* CSPs as search problems, backtracking search

Inference

* **Maintaining arc-consistency**: algorithm for enforcing arc-consistency every time we make a new assignment
* When we make a new assignment to *X*, call AC-3, starting with a queue of all arcs (*Y, X*) where *Y* is a neighbor of *X*

* Minimum remaining values (MRV) heuristic: select the variable that has the smallest domain
* Degree heuristic: select the variable that has the highest degree

* Least-constraining values heuristic: return variables in order by number of choices that are ruled out for neighboring variables. Then try least-constraining first

## 4. Learning

### Supervised learning

...given a data set of input-output pairs, learn a function to map inputs to outputs

* **Classification**: supervised learning task of learning a function mapping an input point to a discrete category

Hypothesis-function *h*

* **Nearest-neighbor classification**: algorithm that, given an input, chooses the class of the nearest data point to that input
* **k-nearest-neighbor classification**: ... chooses the most common class of the *k* nearest data points to that input

#### Linear regression

* Machine learning: estimate the weight vector
* Dot product of weight vector and input vector

* **Perceptron learning rule**, alpha is the learning rate
* **Threshold function**, hard threshold, soft threshold (logistic function)

#### Support Vector Machines

* **Maximum margin separator**: boundary that maximizes the distance between any of the data points
* Finds boundaries which aren't linear through using higher dimensions

#### Regression

...supervised learning task of learning a function mapping an input point to a continuous value

#### Evaluating Hypotheses

Optimization problem of minimizing a **loss function** (function that expresses how poorly our hypothesis performs).

* 0-1 loss function
* L1 loss function
* L2 loss function (penalizes worse predictions, outliers)

Problem: **overfitting**: a model that fits too closely to a particular data set and therefore may fail to generalize to future data

Solution: **regularization**: penalizing hypotheses that are more complex to favor simpler, more general hypotheses

* **holdout cross-validation**: splitting data into a training set and a test set, such that learning happens on the training set and is evaluated on the test set
* **k-fold cross-validation**: splitting data into *k* sets, and experimenting *k* times, using each set as a test set once, and using remaining data as training set

### Reinforcement learning

...given a set of rewards or punishments, learn what actions to take in the future.

* **Markov decision process**: model for decision-making, representing states, actions and their rewards
* **Q-learning**: method for learning a function *Q(s, a)*, estimate of the value of performing action *a* in state *s*
* **Greedy decision-making**: when in state *s*, choose action *a* with highest *Q(s, a)*

Problem: Explore vs. Exploit (knowledge AI already has)

Solution: *epsilon*-greedy algorithm

* **function approximation**: approximating *Q(s, a)*, often by a function combining various features, rather than storing one value for every state-action pair

### Unsupervised learning

...given input data without any additional feedback, learn patterns

* **Clustering**: organizing a set of objects into groups in such a way that similar objects tend to be in the same group
* **k-means clustering**: algorithm for clustering data based on repeatedly assigning points to clusters and updating those clusters' centers

## 5. Neural Networks

Popular activation functions:

* Step function
* Logistic sigmoid
* Rectified linear unit (ReLU)

* **Gradient descent**: algorithm for minimizing loss when training a neural network (gradient for all data points)
* **Stochastic gradient descent**: gradient for 1 data point
* **Mini-batch gradient descent**: gradient for a small batch of data points

* **Perceptron**: only capable of learning linearly separable decision boundary
* **Multilayer neural network**: artificial neural network with an input layer, an output layer and at least one hidden layer
* **Backpropagation**: algorithm for training neural networks with hidden layers
* **Deep neural networks**: neural network with multiple hidden layers

Strategies to combat overfitting of neural networks:

* **dropout**: temporarily removing units (nodes, selected at random) from a neural network to prevent over-reliance on certain units

playground.tensorflow.org

### Computer vision

* **Image convolution**: applying a filter that adds each pixel value of an image to its neighbors, weighted according to a kernel matrix
* **Kernel matrix**, e.g. for edge detection
* **Pooling**: reducing the size of an input by sampling from regions in the input
* **Max-pooling**: choose maximum value for each region

* **Convolutional neural network**: neural network that uses convolution, usually for analyzing images

* **Feed-forward neural network**: neural network that has connections only in one direction
* **Recurrent neural network**: neural network that generates output that feeds back into its own inputs
* **One-to-many relationship**



