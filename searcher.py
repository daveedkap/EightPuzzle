#
# searcher.py (Final project)
#
# classes for objects that perform state-space search on Eight Puzzles  
#
# name: 
# email:
#
# If you worked with a partner, put their contact info below:
# partner's name:
# partner's email:
#

import random
from state import *

class Searcher:
    """ A class for objects that perform random state-space
        search on an Eight Puzzle.
        This will also be used as a superclass of classes for
        other state-space search algorithms.
    """
    ### Add your Searcher method definitions here. ###
    
    def __init__(self, depth_limit):
        """ contrusts a new Searcher object
        """
        self.states = []
        self.num_tested = 0
        self.depth_limit = depth_limit
        
    def add_state(self, new_state):
        """ takes a single State object called new_state and adds it to the Searcher's list of untested states
        """
        self.states += [new_state]
        
    def should_add(self, state):
        """ takes a State object calles state and returns True if the called searcher should add state to its list of untested states and False othewise
        """
        if self.depth_limit != -1 and state.num_moves > self.depth_limit:
                return False
    
        elif state.creates_cycle() == True:
            return False
        
        else:
            return True
    
    def add_states(self, new_states):
        """ takes a list State objects called new_states, and that processes the elements of the new_states one at a time
        """
        for x in new_states:
            if self.should_add(x) == True:
                self.add_state(x)
    
    def next_state(self):
        """ chooses the next state to be tested from the list of 
        untested states, removing it from the list and returning it
        """
        s = random.choice(self.states)
        self.states.remove(s)
        return s
    
    def find_solution(self, init_state):
        """ preforms a full state-space search that begins at the specificed initial state init_state and ends when the goal state is found or when the Searcher runs out of untested states
        """
        self.add_state(init_state)
        
        while self.states:
            temp_state = self.next_state()
            
            self.num_tested += 1
            if temp_state.is_goal():
                return temp_state
            else:
                next_states = temp_state.generate_successors()
                self.add_states(next_states)
        return None

    def __repr__(self):
        """ returns a string representation of the Searcher object
            referred to by self.
        """
        # You should *NOT* change this method.
        s = type(self).__name__ + ': '
        s += str(len(self.states)) + ' untested, '
        s += str(self.num_tested) + ' tested, '
        if self.depth_limit == -1:
            s += 'no depth limit'
        else:
            s += 'depth limit = ' + str(self.depth_limit)
        return s


### Add your BFSeacher and DFSearcher class definitions below. ###

class BFSearcher(Searcher):
    """ a class for objects that searchers and tests the states ith the smallest depth first till it finds the goal or runs out of states to test
    """
    def next_state(self):
        """ overrides the next_state method inhereted from Searcher that chooeses the state that has been in the list for the longest then removes the chosen stte from the untested states before returning it
        """
        s = self.states[0]
        self.states.remove(s)
        return s
    
class DFSearcher(Searcher):
    """ a class for objects that searchers and tests the states with the highest depth firsst till it finds the goal or runs out of states to test
    """
    def next_state(self):
        """ overrides the next_stater method inhereted from Seacher and chooses the state last in the list
        """
        s = self.states[-1]
        self.states.remove(s)
        return s

def h0(state):
    """ a heuristic function that always returns 0 """
    return 0

def h1(state):
    """ a heuristic function that computes and returns an estimate of how many additional moves are needed to get from state to the goal state
    """
    return state.board.num_misplaced()
        
### Add your other heuristic functions here. ###
def h2(state):
    """ a heuristic function that comuptes and returns an estimate of how many additional moves are needed to get from state to the goal state
    """
    index_tile = [0, 1, 2]
    
    row_col = 0
    
    for r in range(len(state.board.tiles)):
        for c in range(len(state.board.tiles[0])):
            num = state.board.tiles[r][c]
            
            if int(num) // 3 != index_tile[r] and num != '0':
                row_col += 1
            if int(num) % 3 != index_tile[c] and num != '0':
                row_col += 1
                
    return row_col

class GreedySearcher(Searcher):
    """ A class for objects that perform an informed greedy state-space
        search on an Eight Puzzle.
    """
    ### Add your GreedySearcher method definitions here. ###
    
    def __init__(self, heuristic):
        """ constructs new GreedySearcher object
        """
        super().__init__(-1)
        self.heuristic = heuristic

    def __repr__(self):
        """ returns a string representation of the GreedySearcher object
            referred to by self.
        """
        # You should *NOT* change this method.
        s = type(self).__name__ + ': '
        s += str(len(self.states)) + ' untested, '
        s += str(self.num_tested) + ' tested, '
        s += 'heuristic ' + self.heuristic.__name__
        return s
    
    def priority(self, state):
        """ computes and returns the priority of the specified state,
        based on the heuristic function used by the searcher
        """
        return -1 * self.heuristic(state)
    
    def add_state(self, state):
        """ overrides the add_state method that is inhereted from Searcher that adds sublist to list of states that holds pritoty of state and the state itself
        """
        self.states += [[self.priority(state), state]]
        
    def next_state(self):
        """ overrides the next_state from Searcher and chooses one of the states with the highest priority
        """
        max_state = max(self.states)
        self.states.remove(max_state)
        return max_state[1]
    
### Add your AStarSeacher class definition below. ###

class AStarSearcher(GreedySearcher):
    """ A class for objects that preform an informed search on an Eight Puzzle
    """
    def priority(self, state):
        return -1 * (self.heuristic(state) + state.num_moves)
    
