import sys
import copy

from crossword import *


class CrosswordCreator():

    def __init__(self, crossword):
        """
        Create new CSP crossword generate.
        """
        self.crossword = crossword
        self.domains = {
            var: self.crossword.words.copy()
            for var in self.crossword.variables
        }

    def __str__(self): #this function prints the values of domain
        #needs to be implemented otherwise Domain returns value in memory
        # Implemented so I can understand better the problem
        return f"Domains:\n {self.domains}"

    def letter_grid(self, assignment):
        """
        Return 2D array representing a given assignment.
        """
        letters = [
            [None for _ in range(self.crossword.width)]
            for _ in range(self.crossword.height)
        ]
        for variable, word in assignment.items():
            direction = variable.direction
            for k in range(len(word)):
                i = variable.i + (k if direction == Variable.DOWN else 0)
                j = variable.j + (k if direction == Variable.ACROSS else 0)
                letters[i][j] = word[k]
        return letters

    def print(self, assignment):
        """
        Print crossword assignment to the terminal.
        """
        letters = self.letter_grid(assignment)
        for i in range(self.crossword.height):
            for j in range(self.crossword.width):
                if self.crossword.structure[i][j]:
                    print(letters[i][j] or " ", end="")
                else:
                    print("█", end="")
            print()

    def save(self, assignment, filename):
        """
        Save crossword assignment to an image file.
        """
        from PIL import Image, ImageDraw, ImageFont
        cell_size = 100
        cell_border = 2
        interior_size = cell_size - 2 * cell_border
        letters = self.letter_grid(assignment)

        # Create a blank canvas
        img = Image.new(
            "RGBA",
            (self.crossword.width * cell_size,
             self.crossword.height * cell_size),
            "black"
        )
        font = ImageFont.truetype("assets/fonts/OpenSans-Regular.ttf", 80)
        draw = ImageDraw.Draw(img)

        for i in range(self.crossword.height):
            for j in range(self.crossword.width):

                rect = [
                    (j * cell_size + cell_border,
                     i * cell_size + cell_border),
                    ((j + 1) * cell_size - cell_border,
                     (i + 1) * cell_size - cell_border)
                ]
                if self.crossword.structure[i][j]:
                    draw.rectangle(rect, fill="white")
                    if letters[i][j]:
                        _, _, w, h = draw.textbbox((0, 0), letters[i][j], font=font)
                        draw.text(
                            (rect[0][0] + ((interior_size - w) / 2),
                             rect[0][1] + ((interior_size - h) / 2) - 10),
                            letters[i][j], fill="black", font=font
                        )

        img.save(filename)

    def solve(self):
        """
        Enforce node and arc consistency, and then solve the CSP.
        """
        self.enforce_node_consistency()
        self.ac3()
        return self.backtrack(dict())

    def enforce_node_consistency(self):
        """
        Update `self.domains` such that each variable is node-consistent.
        (Remove any values that are inconsistent with a variable's unary
         constraints; in this case, the length of the word.)
        """

        #Structure of dic:
        # {Variable(0, 1, 'down', 5): {'FOUR', 'SEVEN', 'ONE', 'FIVE', 'EIGHT', 'TEN', 'NINE', 'SIX', 'TWO', 'THREE'},

        d = copy.deepcopy(self.domains) #create a copy of self.domains to avoid issues while looping

        #print(d)

        for v in self.domains:
            size = v.length #gets the value of size, in our case, last value of key
            for word in self.domains[v]: #loops over all the items of V (all the words)
                if not len(word) == size: #if size of a given word different than assigned size, remove word
                   d[v].remove(word)

        self.domains = copy.deepcopy(d) #update self.domains

        #print(f"SELF-DOMAINS: {self.domains}")

    def revise(self, x, y):
        """
        Make variable `x` arc consistent with variable `y`.
        To do so, remove values from `self.domains[x]` for which there is no
        possible corresponding value for `y` in `self.domains[y]`.

        Return True if a revision was made to the domain of `x`; return
        False if no revision was made.
        """
        if not self.crossword.overlaps[x, y] == None:
            # For any pair of variables v1, v2, their overlap is either:
            #    None, if the two variables do not overlap; or
            #    (i, j), where v1's ith character overlaps v2's jth character

            # get values of i and j where the overlap happens
            i, j = self.crossword.overlaps[x, y]

            #print(f"VALUES of i and j {i}, {j}")

            #create copy of self.domains[x] to avoid issues with iteration
            domains_copy = copy.deepcopy(self.domains)

            #print(f"domains X")
            #print(self.domains[x])
            #print(self.domains)

            #print(f"domains Y")
            #print(self.domains[y])
            #print(domains_copy[y])

            # create boolean to return, initially as False, as nothing was changed
            changed = False

            # iterates over copy and only update original domain
            for word_x in domains_copy[x]:
                #print(f"word_x {word_x}")
                size_domain_y = len(self.domains[y]) # temp variable to check if it is the last word of domain y

                for word_y in domains_copy[y]: #loops over y
                    size_domain_y  -= 1 #decreases the value, to check later of if this is the last chance to match x
                    #print(f"word_y {word_y}")
                    if not word_x[i] == word_y[j]: #if the letters are not compatible...
                        if size_domain_y ==0: # ... and this is the last value to try for y, remove word from X domain
                            self.domains[x].remove(word_x) # remove word from x domain
                            #print(self.domains[x])
                            changed = True #update value to return
                    else: # if the letters were compatible, then goes to check the next word in domain x
                        break
            return changed
        else:
            return False

    def ac3(self, arcs=None):
        """
        Update `self.domains` such that each variable is arc consistent.
        If `arcs` is None, begin with initial list of all arcs in the problem.
        Otherwise, use `arcs` as the initial list of arcs to make consistent.

        Return True if arc consistency is enforced and no domains are empty;
        return False if one or more domains end up empty.
        """
        if arcs is None: #If `arcs` is None, begin with initial list of all arcs in the problem.
            arcs = list()
            for node in self.crossword.variables:
                for neighbour in self.crossword.neighbors(node):
                    if (node, neighbour) not in arcs and (neighbour, node) not in arcs: #avoids duplicates in arc list
                        arcs.append((node, neighbour))

        #print("ARCS")
        #print(len(arcs))

        while len(arcs)>0: #loop until list of arcs is empty
            x, y = arcs[0] #dequeue list of arcs
            arcs.remove((x, y)) #remove tupple from arc

            if self.revise(x, y): #checks if it it possible to have a common word for x and y based on their letters
                if len(self.domains[x]) == 0:
                    return False
                else:
                    arcs_neighbors = self.crossword.neighbors(x)
                    #print(f"arcs neighbours {arcs_neighbors}")
                    for z in arcs_neighbors:
                        if not z==y:
                            arcs.append((z,x)) #enqueue(queue, z, x)
        return True

    def assignment_complete(self, assignment):
        """
        Return True if `assignment` is complete (i.e., assigns a value to each
        crossword variable); return False otherwise.
        """

        #if there are still vars to assign, game is not over
        #if game if not consistent, it is not over
        return (len(self.crossword.variables - assignment.keys()) == 0)

    def consistent(self, assignment):
        """
        Return True if `assignment` is consistent (i.e., words fit in crossword
        puzzle without conflicting characters); return False otherwise.
        """

        # all values are distinct, every value is the correct length,
        # and there are no conflicts between neighboring variables.

        C1, C2, C3 = True, True, True

        # Constraints
        # C1 all values are distinct,
        set_variables_values = set(assignment.values()) # creates a set of values present in the assignment
        if not len(set_variables_values) == len(assignment.items()): #if the size of the created set equals the size of assigment, this step is consistent
            C1 = False

        # C2 every value is the correct length,
        for var in assignment:
            if not var.length == len(assignment[var]):
                C2 = False

        # C3 and there are no conflicts between neighboring variables.
        for var in assignment: #loops over nodes in assigments
            for n in self.crossword.neighbors(var): #loops over neighbours from node
                i, j = self.crossword.overlaps[var, n] #gets the intersection
                if n in assignment: #check if neighboor is already in the assignment
                    if not assignment[var][i] == assignment[n][j]: #if letters not compatible, not consistent
                        C3 = False

        #print(f"CCS {C1}, {C2}, {C3}")
        return C1 and C2 and C3 #if arrived here without returning false, then it is consistent

    def order_domain_values(self, var, assignment):
        """
        Return a list of values in the domain of `var`, in order by
        the number of values they rule out for neighboring variables.
        The first value in the list, for example, should be the one
        that rules out the fewest values among the neighbors of `var`.
        """
        # create list to return, with values and how many values in neighboor nodes it rules out
        least_constraining_values = []

        for value in self.domains[var]: # iterates over all values in var domain
            ruled_out = 0 # initiates rules_out count
            for neighbour in self.crossword.neighbors(var): #iterates over all neighbours of var
                if neighbour not in assignment: #only considers neighbours not already in the assignment
                    for domain_neighbour in self.domains[neighbour]: #iterates of neighbours domains
                        #create a temp assignment, to store var, value and neighbour, domain_neighbour
                        temp_assign = copy.deepcopy(assignment)
                        temp_assign[var] = value
                        temp_assign[neighbour] = domain_neighbour
                        if not self.consistent(temp_assign): #checks if temp assignment is consistent
                            ruled_out +=1 #if not, increases value for rule out
                            #del temp_assign
            least_constraining_values.append((value, ruled_out)) # adds current value, and how many cases it ruled out, to list

        # sort values based on less constraints
        least_constraining_values.sort(key=lambda x: x[1])
        return_least_cv = [ value[0] for value in least_constraining_values ] #we need to return only the words to backtrack, not the count
        #print(f"LCV {return_least_cv}")
        return(return_least_cv)

    def select_unassigned_variable(self, assignment):
        """
        Return an unassigned variable not already part of `assignment`.
        Choose the variable with the minimum number of remaining values
        in its domain. If there is a tie, choose the variable with the highest
        degree. If there is a tie, any of the tied variables are acceptable
        return values.
        """

        unassigned_vars = self.crossword.variables - assignment.keys() #creates a set of unassigned vars

        # creates variables to check VAR with min domain
        tie = False
        min_domain_value, min_domain_var = None, None

        # check for the variable with the minimum number of remaining values
        for var in unassigned_vars:
            if  min_domain_value == None: #initial state
                min_domain_value = len(self.domains[var])
                min_domain_var = var
            else:
                if len(self.domains[var]) < min_domain_value: #if current variable has less domains, updates min_domain_value
                    min_domain_value = len(self.domains[var])
                    min_domain_var = var
                    tie = False #updates value of tie, in case a lower value is found
                elif len(self.domains[var]) == min_domain_value: #if there is a tie, tie = True
                    tie = True

        if not tie: #if there was a tie of
            return min_domain_var

        #if didn't return, proceed to look for var with more neighboors - highest degree
        list_unassigned_neighbours = dict()

        for var in unassigned_vars:
            n_neighbours = len(self.crossword.neighbors(var))
            list_unassigned_neighbours[var] = n_neighbours

        # since we don't care for ties, use max function
        #print(max(list_unassigned_neighbours, key=lambda var: list_unassigned_neighbours[var]))
        return max(list_unassigned_neighbours, key=lambda var: list_unassigned_neighbours[var])



        #return(unassigned_vars.pop())

    def backtrack(self, assignment):
        """
        Using Backtracking Search, take as input a partial assignment for the
        crossword and return a complete assignment if possible to do so.

        `assignment` is a mapping from variables (keys) to words (values).

        If no assignment is possible, return None.
        """
        #print("ASSIGNMENT backtrack")
        #print(assignment)

        # check if assigment is complete, return assignment
        if self.assignment_complete(assignment):
            return assignment #if so, return assignment
        else:
            #backtracking search algorithm from lesson
            var = self.select_unassigned_variable(assignment) #var = select-unassigned-value
            for value in self.order_domain_values(var, assignment): #least-constraining values heuristic ps: takes a while with dataset 2, but works
            #for value in self.domains[var]: #domain values, do not use heuristic
                assignment[var] = value #adds var, value to assignment
                if self.consistent(assignment): #check is new var,value is consistent
                    result = self.backtrack(assignment) #result=backtrack(assignment, csp)
                    if not result==None: #if result not failure
                        return result #return result
                    else:
                        #if resulte is failure remove (var, value) from assignment
                        if isinstance(assignment[var], list): #treats cases where var has a list of values
                            for v in assignment[var]:
                                if v == value:
                                    assignment[var].remove(value)
                        else: #if there is not list of values, just remove by using the key
                            assignment.pop(var)
            return None #return failure


def main():

    # Check usage
    if len(sys.argv) not in [3, 4]:
        sys.exit("Usage: python generate.py structure words [output]")

    # Parse command-line arguments
    structure = sys.argv[1]
    words = sys.argv[2]
    output = sys.argv[3] if len(sys.argv) == 4 else None

    # Generate crossword
    crossword = Crossword(structure, words)
    creator = CrosswordCreator(crossword)
    assignment = creator.solve()

    # Print result
    if assignment is None:
        print("No solution.")
    else:
        creator.print(assignment)
        if output:
            creator.save(assignment, output)


if __name__ == "__main__":
    main()
