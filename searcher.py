#
# searcher.py (Final project)
#
# classes for objects that perform state-space search on Eight Puzzles  
#
# name: Krish Sapru 
# email: ksapru@bu.edu
#
# If you worked with a partner, put his or her contact info below:
# partner's name: Conor Ross 
# partner's email: cbross@bu.edu
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
        """[summary]

        :param depth_limit: [description]
        :type depth_limit: [type]
        """
        
        self.states = []  # -> [init_state]
        self.num_tested = 0 
        self.depth_limit = depth_limit
         
        

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

    def should_add(self, state):
        """[summary]
        :param state: [description]
        :type state: [type]
        :return: [description]
        :rtype: [type]
        """
    
        if (self.depth_limit != -1) and (state.num_moves > self.depth_limit):
            return False
        elif (state.creates_cycle() == True):
            return False
        return True
    
    def add_state(self, new_state):
        """[summary]

        :param new_state: [description]
        :type new_state: [type]
        :return: [description]
        :rtype: [type]
        """
        
        self.states += [new_state]
        
        
    def add_states(self, new_states):
        """[summary]

        :param new_states: [description]
        :type new_states: [type]
        :return: [description]
        :rtype: [type]
        """
        
        for idx in range(len(new_states)):
            if self.should_add(new_states[idx]) == True:
                self.add_state(new_states[idx])      
    
    def next_state(self):
        """ chooses the next state to be tested from the list of 
        untested states, removing it from the list and returning it
        """
        s = random.choice(self.states)
        self.states.remove(s)
        return s         
    

    def find_solution(self, init_state):
        """[summary]

        :param init_state: [description]
        :type init_state: [type]
        :return: [description]
        :rtype: [type]
        """       
        
        self.states += [init_state]
        
        while len(self.states) != 0:
            s = self.next_state()
            if s.is_goal() == True:
                self.num_tested += 1
                return s
            else:
                self.add_states(s.generate_successors())
                self.num_tested += 1
        return None
            
        
    

    ### Add your BFSeacher and DFSearcher class definitions below. ###

class BFSearcher(Searcher):
    """[summary]

    :param searcher: [description]
    :type searcher: [type]
    """

    def next_state(self):
        """[summary]
        """
        
        fifo = self.states[0]
        for idx in range(len(self.states)):
            if self.states[idx].num_moves < fifo.num_moves:
                fifo = self.states[idx]
        self.states.remove(fifo)
        return fifo
        
        

def h0(state):
    """ a heuristic function that always returns 0 """
    return 0

    ### Add your other heuristic functions here. ###

        
def h1(state):
    """[summary]

    :param state: [description]
    :type state: [type]
    :return: [description]
    :rtype: [type]
    """
    return state.board.num_misplaced()  
    
    
 
    
    
class DFSearcher(Searcher):
    """[summary]

    :param Searcher: [description]
    :type Searcher: [type]
    :return: [description]
    :rtype: [type]
    """
    
    def next_state(self):
        """[summary]

        :return: [description]
        :rtype: [type]
        """

        difo = self.states[-1]
        for idx in range(len(self.states)):
           if self.states[idx].num_moves < difo.num_moves:
                difo = self.states[-1]
        self.states.remove(difo)
        return difo
    
    
    
    
class GreedySearcher(Searcher):
    """ A class for objects that perform an informed greedy state-space
        search on an Eight Puzzle.
    """
    ### Add your GreedySearcher method definitions here. ###

    def __init__(self, depth_limit, heuristic):
        """[summary]

        :param init_state: [description]
        :type init_state: [type]
        :param heuristic: [description]
        :type heuristic: [type]
        :param depth_limit: [description]
        :type depth_limit: [type]
        """
        
        super().__init__(depth_limit)
        self.heuristic = heuristic
        self.states = []
        self.num_tested = 0
        
        
        
        
    def priority(self, state):
        """[summary]

        :param state: [description]
        :type state: [type]
        """
        if self.heuristic == -1:
            heuristic = state.board.num_misplaced()
        elif self.heuristic == 1:
            heuristic = state.board.distance()
        return -1 * self.heuristic(state)
    
    def add_state(self, state):
        """[summary]

        :param state: [description]
        :type state: [type]
        """
        
        self.states += [[self.priority(state), state]]
        
        
    def next_state(self):
        """[summary]
        """
        
        self.states.remove(max(self.states))
        return max(self.states)[1]
        
        

        
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


### Add your AStarSeacher class definition below. ###


class AStarSearcher(Searcher):
    """[summary]

    :param Searcher: [description]
    :type Searcher: [type]
    """
    
    def __init__(self, depth_limit, heuristic):
        """[summary]
        """
    
        super().__init__(depth_limit)
        self.heuristic = heuristic
        self.states = []
        self.num_tested = 0
        
        
    def add_state(self, state):
        """[summary]

        :param state: [description]
        :type state: [type]
        """
        
        self.states += [[self.priority(state), state]]
        
        
    def next_state(self):
        """[summary]
        """
        
        self.states.remove(max(self.states))
        return max(self.states)[1]
        
        
    def priority(self, state):
        """[summary]

        :param state: [description]
        :type state: [type]
        """
        if self.heuristic == -1:
            heuristic == state.board.num_misplaced()
        elif self.heuristic == 1:
            heuristic = state.board.distance()
        moves = state.num_moves            
        priority = -1 * (heuristic + num_moves)
        return priority
    
