import itertools
import random
import copy


class Minesweeper():
    """
    Minesweeper game representation
    """

    def __init__(self, height=8, width=8, mines=8):

        # Set initial width, height, and number of mines
        self.height = height
        self.width = width
        self.mines = set()

        # Initialize an empty field with no mines
        self.board = []
        for i in range(self.height):
            row = []
            for j in range(self.width):
                row.append(False)
            self.board.append(row)

        # Add mines randomly
        while len(self.mines) != mines:
            i = random.randrange(height)
            j = random.randrange(width)
            if not self.board[i][j]:
                self.mines.add((i, j))
                self.board[i][j] = True

        # At first, player has found no mines
        self.mines_found = set()

    def print(self):
        """
        Prints a text-based representation
        of where mines are located.
        """
        for i in range(self.height):
            print("--" * self.width + "-")
            for j in range(self.width):
                if self.board[i][j]:
                    print("|X", end="")
                else:
                    print("| ", end="")
            print("|")
        print("--" * self.width + "-")

    def is_mine(self, cell):
        i, j = cell
        return self.board[i][j]

    def nearby_mines(self, cell):
        """
        Returns the number of mines that are
        within one row and column of a given cell,
        not including the cell itself.
        """

        # Keep count of nearby mines
        count = 0

        # Loop over all cells within one row and column
        for i in range(cell[0] - 1, cell[0] + 2):
            for j in range(cell[1] - 1, cell[1] + 2):

                # Ignore the cell itself
                if (i, j) == cell:
                    continue

                # Update count if cell in bounds and is mine
                if 0 <= i < self.height and 0 <= j < self.width:
                    if self.board[i][j]:
                        count += 1

        return count

    def won(self):
        """
        Checks if all mines have been flagged.
        """
        return self.mines_found == self.mines


class Sentence():
    """
    Logical statement about a Minesweeper game
    A sentence consists of a set of board cells,
    and a count of the number of those cells which are mines.
    """

    def __init__(self, cells, count):
        self.cells = set(cells)
        self.count = count

    def __eq__(self, other):
        return self.cells == other.cells and self.count == other.count

    def __str__(self):
        return f"{self.cells} = {self.count}"

    def known_mines(self):
        """
        Returns the set of all cells in self.cells known to be mines.
        """
        #I know all sentence's cells are mines if the len of the set equals the count of bombs
        if self.count == len(self.cells):
            return self.cells

    def known_safes(self):
        """
        Returns the set of all cells in self.cells known to be safe.
        """

        #If the count is 0, all cells in set are safe
        if self.count == 0:
            return self.cells

    def mark_mine(self, cell):
        """
        Updates internal knowledge representation given the fact that
        a cell is known to be a mine.
        """
        # first check to see if cell is one of the cells included in the sentence.
        if cell in self.cells:
            # If cell is in the sentence, the function should update the sentence
            # so that cell is no longer in the sentence,
            # but still represents a logically correct sentence
            # given that cell is known to be a mine.

            self.cells.remove(cell)
            self.count -= 1 #there will be one less mine in set

        #If cell is not in the sentence, then no action is necessary.


    def mark_safe(self, cell):
        """
        Updates internal knowledge representation given the fact that
        a cell is known to be safe.
        """

        #first check to see if cell is one of the cells included in the sentence.
        if cell in self.cells:
            #If cell is in the sentence, the function should update the sentence
            # so that cell is no longer in the sentence,
            # but still represents a logically correct sentence given that cell is known to be safe.
            self.cells.remove(cell)
            # there is no need to update count, as self.count counts only mines



class MinesweeperAI():
    """
    Minesweeper game player
    """

    def __init__(self, height=8, width=8):

        # Set initial height and width
        self.height = height
        self.width = width

        # Keep track of which cells have been clicked on
        self.moves_made = set()

        # Keep track of cells known to be safe or mines
        self.mines = set()
        self.safes = set()

        # List of sentences about the game known to be true
        self.knowledge = []

    def mark_mine(self, cell):
        """
        Marks a cell as a mine, and updates all knowledge
        to mark that cell as a mine as well.
        """
        self.mines.add(cell)
        for sentence in self.knowledge:
            sentence.mark_mine(cell)

    def mark_safe(self, cell):
        """
        Marks a cell as safe, and updates all knowledge
        to mark that cell as safe as well.
        """
        self.safes.add(cell)
        for sentence in self.knowledge:
            sentence.mark_safe(cell)

    def add_knowledge(self, cell, count):
        """
        Called when the Minesweeper board tells us, for a given
        safe cell, how many neighboring cells have mines in them.

        This function should:
            1) mark the cell as a move that has been made
            2) mark the cell as safe
            3) add a new sentence to the AI's knowledge base
               based on the value of `cell` and `count`
            4) mark any additional cells as safe or as mines
               if it can be concluded based on the AI's knowledge base
            5) add any new sentences to the AI's knowledge base
               if they can be inferred from existing knowledge
        """

        #print(cell, count)

        # mark the cell as one of the moves made in the game.
        self.moves_made.add(cell)

        #  mark the cell as a safe cell, updating any sentences that contain the cell as well.
        self.mark_safe(cell)


        # The function should add a new sentence to the AI’s knowledge base,
        # based on the value of cell and count, to indicate that
        # count of the cell’s neighbors are mines.
        # Be sure to only include cells whose state is still undetermined in the sentence.


        # first, creates a set with all cells around a given cell
        around_cell =  set()

        row, col = cell[0], cell[1] # to read better, gets coordinates of cell

        #this loop will go around all cells around given cell, ignoring the cells outside range
        # incrementals in range function need extra +1, to stop at row+1, col+1
        # do not include current cell
        # treat height and width with -1 to keep in board range
        for x in range(row-1, row+2):
            for y in range(col-1, col+2):
                if 0 <= x <= self.height-1 and 0<= y <= self.width-1 and not (x==row and y==col):
                    around_cell.add((x,y))

        #print("Around cell")
        #print(around_cell)

        #the next thing I can do, is mark all cells arounc cell as safe, if count =0
        # IMPORTANT: Do not add learning, as cell is marked as SAFE
        if count == 0:
            for c in around_cell:
                self.mark_safe(c)
                #sentence = Sentence(around_cell, count)
                #self.knowledge.append(sentence)
        # likewise, if count == lenght of around cell, then they are all bombs
        elif count == len(around_cell):
            for c in around_cell:
                self.mark_mine(c)
                #sentence = Sentence(around_cell, count)
                #self.knowledge.append(sentence)
        else:
            # Add learning, based on cells around given cell
            sentence = Sentence(around_cell, count)
            self.knowledge.append(sentence)
            #print("SENTENCE")
            #print(sentence)

        # create a subset of known bombs around a cell
        subset_mines_around_cell = around_cell.intersection(self.mines)

        # create a subset of unknown cells around a cell
        unknown_around = around_cell - self.mines - self.safes
        unknown_count = count - len(subset_mines_around_cell)

         #adds this as information
        if  len(unknown_around) > 0 and not unknown_around == around_cell:
            sentence = Sentence(unknown_around, unknown_count)
            self.knowledge.append(sentence)

        print("Unknow around set, count")
        print(unknown_around)
        print(unknown_count)

        print("Len subset_mines_around_cell")
        print(len(subset_mines_around_cell))


        print("SAFES: ")
        print(self.safes)

        print("MINES")
        print(self.mines)

        #Be careful not to modify a set while iterating over it. Doing so may result in errors!
        #Now I will check if my knowledge base
        copy_kb = copy.deepcopy(self.knowledge)

        for s in copy_kb:
            #if there is only one cell, and count is one, we have a bomb
            if len(s.cells) == 1 and s.count == 1:
                for i, j in s.cells:
                    self.mark_mine((i,j))
            elif s.count == 0: #if count is zero, all cells are safe
                for i, j in s.cells:
                    self.mark_safe((i,j))

        copy_kb2 = copy.deepcopy(copy_kb)

        # Get all combinations of 2 sets from copy_kb
        #combinations_copy_kb = list(itertools.combinations(copy_kb, 2))
        #for pair in combinations_copy_kb:
        #    new_sentence=search_subset(pair[0],pair[1])
        #    print(new_sentence)
        #    if (new_sentence):
        #        self.knowledge.append(new_sentence)

        #temp_KB removes all empty sets from KB, then updates KB
        temp_KB = [s for s in self.knowledge if s]
        self.knowledge = temp_KB

        print("KB")
        for s in self.knowledge:
            #if len(s.cells) == 0:
                #self.knowledge.remove(s)
            print(s)
        print("################################")

    def make_safe_move(self):
        """
        Returns a safe cell to choose on the Minesweeper board.
        The move must be known to be safe, and not already a move
        that has been made.

        This function may use the knowledge in self.mines, self.safes
        and self.moves_made, but should not modify any of those values.
        """

        for safe in self.safes: #Tries to find self move
            if safe not in self.moves_made and safe not in self.mines: #tries to find safe move that has not been made
                return safe

        #if safe move not found, returns none
        return None

    def make_random_move(self):
        """
        Returns a move to make on the Minesweeper board.
        Should choose randomly among cells that:
            1) have not already been chosen, and
            2) are not known to be mines
        """

        #loops until valid move, with a maximum of empty spaces
        # first calculate empty spaces
        empty = (self.height * self.width) - len(self.moves_made) - len(self.mines)
        while empty > 0:
            #creates a random value for i and j based on board size
            i, j = random.randint(0, self.height-1), random.randint(0, self.width-1)

            if not (i,j) in self.moves_made and not (i,j) in self.mines:
                #print(i, j)
                return (i,j)
            else:
                empty -=1  #updates empty and runs the loop again

        #if no random value found, them game is over, or if empty == 0, because only empty spaces are bombs
        return None

# function search subset
def search_subset(sentence1, sentence2):
    """ This function gets two subsets,
    and if one contains the other, returns a new Sentence for KB
    else returns None """
    if sentence1 == sentence2:
        print("search_subset1")
        return None
    if sentence1.cells.issubset(sentence2.cells):
        new_sentence = Sentence (sentence2.cells-sentence1.cells, sentence2.count-sentence1.count)
        print("s1 subset de s2")
        return new_sentence
    elif sentence2.cells.issubset(sentence1.cells):
        new_sentence = Sentence (sentence1.cells-sentence2.cells, sentence1.count-sentence2.count)
        print("s2 subset de s1")
        print(new_sentence)
        return new_sentence
    else:
        print("search_subset2")
        return None

