# finalproject1




class Board:
    """ A class for objects that represent an Eight Puzzle board.
    """
    def __init__(self, digitstr):
        """ a constructor for a Board object whose configuration
            is specified by the input digitstr
            input: digitstr is a permutation of the digits 0-9
        """
        # check that digitstr is 9-character string
        # containing all digits from 0-9
        assert(len(digitstr) == 9)
        for x in range(9):
            assert(str(x) in digitstr)

        self.tiles = [[0] * 3 for x in range(3)]
        self.blank_r = -1
        self.blank_c = -1

        # Put your code for  the rest of __init__ below.
        # Do *NOT* remove our code above.
        for r in range(len(self.tiles)):
            for c in range(len(self.tiles[0])): 
                self.titles[r][c] = int(digitstr[3*r + c])
                if int(digitstr[3*r + c]) == 0):
                    self.blank_r = r
                    self.blank_c = c

    ### Add your other method definitions below. ###


    
    def __repr__(self):
        """[summary]
        """
        for r in range(0,3):
            for c in range(0,3):
                if (self.tiles[r][c] is not 0):
                    s += str(self.tiles[r][c] + '')
                else:
                    s += '_' + '\n'
                return s 
                
                
