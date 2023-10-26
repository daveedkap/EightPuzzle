#
# board.py (Final project)
#
# A Board class for the Eight Puzzle
#
# name: Tonito Abello
# email: teabello@bu.edu
#
# If you worked with a partner, put their contact info below:
# partner's name: David Kaplansky
# partner's email: davidkap@bu.edu
#

# a 2-D list that corresponds to the tiles in the goal state
GOAL_TILES = [['0', '1', '2'],
              ['3', '4', '5'],
              ['6', '7', '8']]

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

        self.tiles = [[''] * 3 for x in range(3)]
        self.blank_r = -1
        self.blank_c = -1

        # Put your code for the rest of __init__ below.
        # Do *NOT* remove our code above.
        
        for r in range(3):
            for c in range(3):
                index = (3*r + c)
                self.tiles[r][c] = digitstr[index]
                if digitstr[index] == '0':
                    self.blank_r = r
                    self.blank_c = c


    ### Add your other method definitions below. ###
    
    def __repr__(self):
        """ returns a string reprentation of a Board object
        """
        s = ''
        for i in range(len(self.tiles)):
            for j in range(len(self.tiles[0])):
                if i == 0:
                    if j == 2:
                        if self.tiles[i][j] == '0':
                            s += '_' + ' \n'
                        else:
                            s += self.tiles[i][j] + ' \n'
                    else:
                        if self.tiles[i][j] == '0':
                            s += '_' + ' '
                        else:
                            s += self.tiles[i][j] + ' '
                elif i == 1:
                    if j == 2:
                        if self.tiles[i][j] == '0':
                            s += '_' + ' \n'
                        else:
                            s += self.tiles[i][j] + ' \n'
                    else:
                        if self.tiles[i][j] == '0':
                            s += '_' + ' '
                        else:
                            s += self.tiles[i][j] + ' '
                else:
                    if j == 2:
                        if self.tiles[i][j] == '0':
                            s += '_' + ' \n'
                        else:
                            s += self.tiles[i][j] + ' \n'
                    else:
                        if self.tiles[i][j] == '0':
                            s += '_' + ' '
                        else:
                            s += self.tiles[i][j] + ' '
        return s
    
    def move_blank(self, direction):
        """ takes an input and makes a string direction that specifies which direction the blank should move, then mdodifes the board and returns true if this motion is possible, if not possible returns false 
        """
        temp_r = self.blank_r
        temp_c = self.blank_c
        
        if direction != 'up' and direction != 'down' and direction != 'left' and direction != 'right':
            return False
        elif direction == 'up':
            temp_r = int(temp_r) - 1
            if temp_r not in range(3):
                return False
        elif direction == 'down':
            temp_r = int(temp_r) + 1
            if temp_r not in range(3):
                return False
        elif direction == 'left':
            temp_c = int(temp_c) - 1
            if temp_c not in range(3):
                return False
        elif direction == 'right':
            temp_c = int(temp_c) + 1
            if temp_c not in range(3):
                return False
        
        for i in range(len(self.tiles)):
            for j in range(len(self.tiles[0])):
                if self.tiles[i][j] == '0':
                    if direction == 'up':
                        num = self.tiles[i-1][j]
                        self.tiles[i][j] = num
                        self.tiles[i-1][j] = '0'
                        for i in range(len(self.tiles)):
                            for j in range(len(self.tiles[0])):
                                if self.tiles[i][j] == '0':
                                    self.blank_r = i
                                    self.blank_c = j
                        return True
                    elif direction == 'down':
                        num = self.tiles[i+1][j]
                        self.tiles[i][j] = num
                        self.tiles[i+1][j] = '0'
                        for i in range(len(self.tiles)):
                            for j in range(len(self.tiles[0])):
                                if self.tiles[i][j] == '0':
                                    self.blank_r = i
                                    self.blank_c = j
                        return True
                    elif direction == 'left':
                        num = self.tiles[i][j-1]
                        self.tiles[i][j] = num
                        self.tiles[i][j-1] = '0'
                        for i in range(len(self.tiles)):
                            for j in range(len(self.tiles[0])):
                                if self.tiles[i][j] == '0':
                                    self.blank_r = i
                                    self.blank_c = j
                        return True
                    elif direction == 'right':
                        num = self.tiles[i][j+1]
                        self.tiles[i][j] = num
                        self.tiles[i][j+1] = '0'
                        for i in range(len(self.tiles)):
                            for j in range(len(self.tiles[0])):
                                if self.tiles[i][j] == '0':
                                    self.blank_r = i
                                    self.blank_c = j
                        return True
                    
    def digit_string(self):
        """ creates and return sa string of digits corresponding to the current ones in the board
        """
        ds = ''
        for i in range(len(self.tiles)):
            for j in range(len(self.tiles[0])):
                num = self.tiles[i][j]
                ds += num
        return ds
    
    def copy(self):
        """ returns a newly-constructed Board object that is a deep copy of the object called 
        """
        new_board = Board(self.digit_string())
        return new_board
    
    def num_misplaced(self):
        """ counts and returns the number of tiles in the called Board that are not where they should be in the goal state
        """
        count = 0
        
        for i in range(len(self.tiles)):
            for j in range(len(self.tiles[0])):
                if self.tiles[i][j] == '0':
                    count += 0
                else:
                    if self.tiles[i][j] != GOAL_TILES[i][j]:
                        count += 1
        
        return count    

    def __eq__(self, other):
        """ can be called when the == operator is used to compare two board objects, returns True if called object is same as other object and False if not equal or same
        """
        return self.tiles == other.tiles
    
    
        
