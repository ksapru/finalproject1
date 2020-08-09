#
# board.py (Final project)
#
# A Board class for the Eight Puzzle
#
# name:
# email:
#
# If you worked with a partner, put his or her contact info below:
# partner's name:
# partner's email:
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
        """[summary]
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
        """[summary]
        :param direction: [description]
        :type direction: [type]
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
        """[summary]
        """
        s = ''
        for r in range(len(self.tiles)):
            for c in range(len(self.tiles[0])):
                s += str(self.tiles[r][c])
                
        return s 
    
    def copy(self):
        """[summary]
        """
        digits = self.digit_string()
        new_board = Board(digits)
        return new_board
        
    
    def num_misplaced(self):
        """[summary]
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
        """[summary]
        :param other: [description]
        :type other: [type]
        """
        
        if (self.tiles == other.tiles):
            return True 
        return False 
 
