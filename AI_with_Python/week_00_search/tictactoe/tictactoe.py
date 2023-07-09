"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None

def main():
    board = initial_state()
    print(transform(board))
    print (winner(board))
    print(terminal(board))
    #print(player(board))

def initial_state():
    """
    Returns starting state of the board.
    """
    #return [[O, X, X],
    #        [X, EMPTY, O],
    #        [O, X, X]]

    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """

    if board == initial_state(): #if the board has the innitial state
        return X # then X plays first
    else: #if the game is already happening
        #counts how many X and O to decide next player
        x_play = o_play = 0 #initiate x_play and o_play

        #loops over board to count how many turns each player had
        for i in range(3):
            for j in range(3):
                if board[i][j] == X:
                    x_play += 1
                elif board[i][j] == O:
                    o_play += 1

        #decide whose turn is next based on count
        if x_play > o_play:
            return O
        else:
            return X

def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """

    list_actions = set() # create a set to return all (i,j) empty places

    for i in range(3): #iterate over each row in the board
        for j in range(3): #iterate over each column in the board
            element = board[i][j]
            if element == EMPTY: # if board element is empty
                list_actions.add((i,j)) # add tuple (i,j) to the list of possible actions

    return list_actions # return list of possible actions

def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """


    if not len(action) == 2: #checks if action is in the format i, j
        raise Exception("Incorrect action")

    # create a deep copy of board
    board_copy = copy.deepcopy(board)

    #initiate i and j based on action values
    i = action[0] # initiate index i
    j = action[1] # initiate index j

    if board[i][j] == None and 0 <= i <= 2 and 0 <= j <= 2: # check is values i,j are valid
        board_copy[i][j] =  player(board) #update board with value for current player
    else:
        raise Exception("Invalid move") # raise exception if invalid values

    return board_copy #return board with given action


def transform(board):
    """
        Transforms a board into a list of -1 for O, 0 for EMPTY and 1 for X
    """
    t_board = [[0, 0, 0] for _ in range(3)]  # Initialize t_board as a 3x3 matrix of zeros
    for i in range(3):
        for j in range(3):

            value = board[i][j]
            #using it-elif-else instead of match for python versions prior to 3.10
            if value is None:
                t_board[i][j] = 0
            elif value == 'X':
                t_board[i][j] = 1
            elif value == 'O':
                t_board[i][j] = -1
            else:
                raise Exception("Error, not valid value on board")
    return t_board

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    board_formated = transform(board) #gets a version of board formated with 1, 0 and -1

    temp_sum = 0 #temp_sum that will enter loops

    # check sum of all rows
    # a row with an element will have value 1 or -1
    # returns winner if any winner on row, otherwise proceed to check winner in columns and diagonal
    for i in range(3):
        for j in range(3):
            #every time enters the loop, adds value of element to temp_sum
            temp_sum = board_formated[i][j] + temp_sum
            #when arrives at the end of a column, check if sum is 3 or -3
            if ((j == 2) and (temp_sum == 3 or temp_sum == -3)):
                if temp_sum == 3:
                    return X
                else:
                    return O
            elif j==2:
                temp_sum = 0 # if sum is not 3 or -3, there is no winner in row, resets temp_sum
    # check sum of all columns
    # returns winner, if winner or column, otherwise continue to check on diagonal
    for i in range(3):
        for j in range(3):
            #every time enters the loop, adds value of element to temp_sum
            temp_sum += board_formated[j][i]
            #when arrives at the end of a column, check if sum is 3 or -3
            if j == 2 and (temp_sum == 3 or temp_sum == -3):
                if temp_sum == 3:
                    return X
                elif temp_sum== -3:
                    return O
            elif j==2:
                temp_sum = 0
                 # if sum is not 3 or -3, there is no winner in row, resets temp_sum

    #check sum of diagonal, based on position of tictactoe board
    sum_d1 = board_formated[0][0] + board_formated[1][1] + board_formated [2][2]
    sum_d2 = board_formated[2][0] + board_formated[1][1] + board_formated [0][2]

    if sum_d1 == 3 or sum_d2 == 3: #check if X wins in any diagonal
        return X
    elif sum_d1 == -3 or sum_d2 == -3: #check if O wins in any diagonal
        return O
    else: None #if got up to here and no return, then no winner yet


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board)==None:
        for i in range(3):
            for j in range (3):
                if board[i][j] == EMPTY: #if there is still empty spaces, game is not over
                    return False
                elif i == 2 and j==2 and not board[i][j]==EMPTY: # if there are no empty cells
                    return True #game is over, it is a draw
    else: #if the winner function returns other than None, game is over, there is a winner
        return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    w = winner(board)

    if w == X:
        return 1
    elif w == O:
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """

    if terminal(board): #if game is over
        return None #returns none

    p = player(board) #checks who is the player
    optimal_action = None #initiate optimal action to return

    if p== X: #if it is X turn, tries to find min value
        score = -100000 #infinite low value to compare

        for action in actions(board): #check possible actions on the board
            min_score = minvalue(result(board, action)) #get the lowest possible score
            #print("Min", min_score, score)
            if min_score > score: #if min_score is lowest than current score, update score and optimal action
                score = min_score
                optimal_action = action

        return optimal_action

    elif p== O:
        score = 100000 #infinite high value to compare

        for action in actions(board): #check possible actions on the board
            max_score = maxvalue(result(board, action)) #get the maximum possible score
            #print("Max", max_score, score)
            if max_score < score: #if maximum score is higher than score, update score and optimal action
                score = max_score
                optimal_action = action

        return optimal_action


def maxvalue(board):

    if terminal(board): #if game is over
        return utility(board) #returns utility board

    min_score = -100000 #initiate a variable min_score with infinite negative value

    for action in actions(board):
        min_score = max(min_score, minvalue(result(board, action))) #returns the highest minimum value found

    return min_score

def minvalue(board):

    if terminal(board): #if game is over
        return utility(board) #returns utility board

    max_score = 100000 #initiate a variable max_score with infinite value

    for action in actions(board):
        max_score = min(max_score, maxvalue(result(board, action))) #returns the smallest maximum value found

    return max_score



if __name__ == "__main__":
    main()
