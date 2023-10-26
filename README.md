# 8-Puzzle

## Description
My take on the classic eight-puzzle presents a way to represent the state of a puzzle using both uninformed (random, BFS, DFS) and informed (Greedy, A* Search) search strategies. Additionally, heuristic functions allow the program to make informed decisions about which states are more promising than others based on calculated estimates.

## Features
- State-Space Search Algorithms: The Searcher class of my program demonstrates a state-space searcher, randomly selecting states to test. Subclasses of Searcher, including BFSearcher, DFSearcher, GreedySearcher, and AStarSearcher, use specific state-space search strategies, whereas the BFSearcher and DFSearcher represent states tested based on their time of addition. The GreedySearcher utilizes a heuristic approach to prioritize states based on an estimated cost to reach the goal, while AStarSearcher expands on this by combining the heuristic with the number of moves already taken to reach a state.

- Heuristics: The program introduces heuristic functions (h0, h1, and h2) that provide estimates of the cost to reach the goal from a given state. h0 always returns 0, serving as a base case. h1 counts the number of misplaced tiles, and h2 calculates the row and column displacements of tiles from their goal positions. These heuristic functions are necessary for informed search strategies like GreedySearcher and AStarSearcher to function properly.
