import random
from state import *

class Searcher:
    """ A class for objects that perform random state-space
        search on an Eight Puzzle.
        This will also be used as a superclass of classes for
        other state-space search algorithms.
    """
    ### Add your Searcher method definitions here. ###

    def __init__(self, init.state, depth_limit):
        """[summary]

        :param depth_limit: [description]
        :type depth_limit: [type]
        """
        
        self.states = [init_state]
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


### Add your BFSeacher and DFSearcher class definitions below. ###



def h0(state):
    """ a heuristic function that always returns 0 """
    return 0

### Add your other heuristic functions here. ###


def should_add(self, state):
    """[summary]

    :param state: [description]
    :type state: [type]
    :return: [description]
    :rtype: [type]
    """
    
    

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

