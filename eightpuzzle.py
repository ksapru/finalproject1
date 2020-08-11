#
# eight_puzzle.py (Final Project)
#
# driver/test code for state-space search on Eight Puzzles
#
# name: Krish Sapru 
# email: ksapru@bu.edu
#
# If you worked with a partner, put his or her contact info below:
# partner's name: Conor Ross
# partner's email: cbross@bu.edu
#

from searcher import *
from timer import *

def create_searcher(algorithm, extra = -1):
    """ a function that creates and returns an appropriate
        searcher object, based on the specified inputs. 
        inputs:
          * algorithm - a string specifying which algorithm the searcher
              should implement
          * extra - an optional extra parameter that can be used to
            specify either a depth limit or the number of a heuristic function
        Note: If an unknown value is passed in for the algorithm parameter,
        the function returns None.
    """
    searcher = None
    
    if algorithm == 'random':
        searcher = Searcher(depth_limit)
    elif algorithm == 'BFS':
        searcher = BFSearcher(extra)
    elif algorithm == 'DFS':
        searcher = DFSearcher(extra)
    elif algorithm == 'Greedy':
        searcher = GreedySearcher(extra, -1)
    elif algorithm == 'A*':
        searcher = AStarSearcher(extra, -1)
    else:  
        print('unknown algorithm:', algorithm)

    return searcher

def eight_puzzle(init_boardstr, algorithm, extra=-1):
    """ a driver function for solving Eight Puzzles using state-space search
        inputs:
          * init_boardstr - a string of digits specifying the configuration
            of the board in the initial state
          * algorithm - a string specifying which algorithm you want to use
          * extra - an optional extra parameter that can be used to
            specify either a depth limit or the number of a heuristic function
    """
    init_board = Board(init_boardstr)
    init_state = State(init_board, None, 'init')

    searcher = create_searcher(algorithm, extra)
    if searcher == None:
        return

    soln = None
    timer = Timer(algorithm)
    timer.start()
    
    try:
        soln = searcher.find_solution(init_state)
    except KeyboardInterrupt:
        print('Search terminated.')

    timer.end()
    print(str(timer) + ', ', end='')
    print(searcher.num_tested, 'states')

    if soln == None:
        print('Failed to find a solution.')
    else:
        print('Found a solution requiring', soln.num_moves, 'moves.')
        show_steps = input('Show the moves (y/n)? ')
        if show_steps == 'y':
            soln.print_moves_to()



def process_file(filename, algorithm, depth_limit=-1, heuristic=None):
    """ doctring goes here
    """
    
    file = open(filename, 'r')
    for line in file:
        line = line[:-1]
        board = Board(line)
        init_state = State(board, None, 'init')
        if algorithm == 'random':
            searcher = Searcher(init_state, extra)
        elif algorithm == 'BFS':
           searcher = BFSearcher(init_state, extra)
        elif algorithm == 'DFS':
           searcher = DFSearcher(init_state, extra)
        elif algorithm == 'Greedy':
           searcher = GreedySearcher(init_state, extra, -1)
        elif algorithm == 'A*':
           searcher = AStarSearcher(init_state, extra, -1)
        else:  
            print('unknown algorithm:', algorithm)
        sol = None
        try:
            soln = searcher.find_solution(s)
        except KeyboardInterrupt:
            idx = line + ': ' + 'search terminated, no solution'
            print(idx)
            count -= 5
            total -= searcher.num_tested
            total2 -= sol.num_moves 
        if sol == None:
            idx = line + ': ' + 'no solution'
            print(idx)
        elif sol != None:
            count += 1
            tot1 += searcher.num_tested
            tot2 += sol.num_moves
            idx = line + ': ' + str(sol.num_moves)+ ' moves, ' + str(searcher.num_tested) + ' states tested'
            print(idx)
    if count == 0:
        print('\nsolved 0 puzzles')
    else:
        
      
