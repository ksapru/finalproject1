#
# board.py (Final project)
#
# A Board class for the Eight Puzzle
#
# name: Krish Sapru
# email: ksapru@bu.edu
#
# If you worked with a partner, put his or her contact info below:
# partner's name: Conor Ross
# partner's email: cbross@bu.edu
#






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
                self.tiles[r][c] = int(digitstr[3*r + c])
                if int(digitstr[3*r + c]) == 0:
                    self.blank_r = r
                    self.blank_c = c

    ### Add your other method definitions below. ###


    
    def __repr__(self):
        """returns a string representation of a Board object.
        """
        s = ''
        for r in range(len(self.tiles)):
            for c in range(len(self.tiles[0])):
                if self.tiles[r][c] == 0:
                    s += '_ '
                else:
                    s += str(self.tiles[r][c]) + ' '
            s += '\n'
            
        return s
    
    
    def move_blank(self, direction):
        """takes as input a string direction that specifies 
            the direction in which the blank should move, and that 
            attempts to modify the contents of the called Board object accordingly.
        :param direction: specifies the direction in which the blank should move 
        :type direction: str
        """
        choices = 'up, down, left, right'
        if direction not in choices:
            print('Error: Please enter a valid direction!')
            return False 
         
        row = self.blank_r
        col = self.blank_c
        
        if direction == 'down':
            if row + 1 <= len(self.tiles) - 1:
                blank = self.tiles[row][col]
                new_blank = self.tiles[row + 1][col]
                self.tiles[row + 1][col] = blank
                self.tiles[row][col] = new_blank 
                self.blank_r = row + 1
                return True 
            return False 
    
        if direction == 'up':
            if row - 1 <= len(self.tiles) + 1:
                blank = self.tiles[row][col]
                new_blank = self.tiles[row - 1][col]
                self.tiles[row][col] = new_blank
                self.tiles[row - 1][col] = blank
                self.blank_r = row - 1
                return True 
            return False 
        
        if direction == 'right':
            if col + 1 <= len(self.tiles[0]) - 1:
                blank = self.tiles[row][col]
                new_blank = self.tiles[row][col + 1]
                self.tiles[row][col + 1] = blank
                self.tiles[row][col] = new_blank
                self.blank_c = col + 1
                return True 
            return False 
                
        if direction == 'left':
            if col - 1 <= len(self.tiles[0]) + 1:
                blank = self.tiles[row][col]
                new_blank = self.tiles[row][col - 1]
                self.tiles[row][col - 1] = blank
                self.tiles[row][col] = new_blank
                self.blank_c = col - 1
                return True
            return False 
            
        
                        
    def digit_string(self):
        """ returns a string of digits that corresponds to the 
            current contents of the called Board object’s tiles attribute.
        """
        s = ''
        for r in range(len(self.tiles)):
            for c in range(len(self.tiles[0])):
                s += str(self.tiles[r][c])
                
        return s 
    
    def copy(self):
        """ copies the digit string into a new self object
        """
        digits = self.digit_string()
        new_board = Board(digits)
        return new_board
        
    
    def num_misplaced(self):
        """returns a newly-constructed Board object 
            that is a deep copy of the called object
        """
        
        count = 0 
        num = 0
        if self.blank_c == 0 and self.blank_r == 0:
            count = 1
        existing_board = self.digit_string()
        for idx in existing_board:
            if int(idx) != num:
                count += 1
            else:
                count += 0
            num += 1

        return count - 1
        
        
                
    def __eq__(self, other):
        """ return True if the called object (self) and the argument (other) 
            have the same values for the tiles attribute, and False otherwise.
        :param other: the other object to which self is being compared to the self object 
        :type other: arguement
        """
        
        if (self.tiles == other.tiles):
            return True 
        return False 
 
