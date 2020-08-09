#
# searcher.py (Final project)
#
# classes for objects that perform state-space search on Eight Puzzles  
#
# name: 
# email:
#
# If you worked with a partner, put his or her contact info below:
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
    
        if (self.depth_limit != -1) and (state.num_moves > self.depth_limit) and (state.creates_cycle() == True):
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
        
        for idx in new_states:
            if self.should_add(idx) == True:
                self.add_state(idx)         
    
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
        
        self.state += [init_state]
        
        while len(self.states) != 0:
            test = self.next_state()
            
            if test.is_goal() == True:
                self.num_tested += 1 
                return test
            else:
                test_succ = self.generate_succesors(test)
                self.add_state = self.generate_successors(test)
                self.add
        return None
        
    

### Add your BFSeacher and DFSearcher class definitions below. ###



def h0(state):
    """ a heuristic function that always returns 0 """
    return 0

### Add your other heuristic functions here. ###



class GreedySearcher(Searcher):
    """ A class for objects that perform an informed greedy state-space
        search on an Eight Puzzle.
    """
    ### Add your GreedySearcher method definitions here. ###


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

