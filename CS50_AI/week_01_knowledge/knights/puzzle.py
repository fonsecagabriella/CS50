from logic import *

AKnight = Symbol("A is a Knight")
AKnave = Symbol("A is a Knave")

BKnight = Symbol("B is a Knight")
BKnave = Symbol("B is a Knave")

CKnight = Symbol("C is a Knight")
CKnave = Symbol("C is a Knave")

# Puzzle 0
# A says "I am both a knight and a knave."
knowledge0 = And(

    #REMEMBER: knight tells the truth, knave lies

    Or(AKnave, AKnight), #A is a knave or a knight
    Not(And(AKnave, AKnight)), #they cannot be both

    # If A is AKnight, then what he says should be true
    Implication(AKnight, And(AKnight, AKnave)),

    #If A is AKnave, then what he says should be false
    Implication(AKnave, Not(And(BKnave, AKnave)))

    # OR OPTION TWO
    # More efficient, but a little harder to understand
    # If A is a nave, it implies he is not saying the truth
    # He is not saying the truth, he is a nave
   # Biconditional(AKnave, Not(And(AKnave,AKnight)))
)


# Puzzle 1
# A says "We are both knaves."
# B says nothing.
knowledge1 = And(

    Or(AKnave, AKnight), #A is a knave or a knight
    Not(And(AKnave, AKnight)), #they cannot be both

    Or(BKnave, BKnight), #B is a knave or a knight
    Not(And(BKnave, BKnight)), #they cannot be both

    #if A is AKnight, then what he says should be true
    Implication(AKnight, And(BKnave, AKnave)),
    #If A is AKnave, then what he says should be false
    Implication(AKnave, Not(And(BKnave, AKnave)))

)

# Puzzle 2
# A says "We are the same kind."
# B says "We are of different kinds."
knowledge2 = And(
    Or(AKnave, AKnight), #A is a knave or a knight
    Not(And(AKnave, AKnight)), #they cannot be both

    Or(BKnave, BKnight), #B is a knave or a knight
    Not(And(BKnave, BKnight)), #they cannot be both

    #if A is AKnight, then what he says should be true: We are the same kind
    # otherwise, what he says is false
    Implication(AKnight, Or(And(AKnight, BKnight),And(AKnave, BKnave))),
    Implication(AKnave, Not(Or(And(AKnight, BKnight),And(AKnave, BKnave)))),

    #if B is AKnight, then what he says should be true: We are of different kinds
    # otherwise what he says is false
    Implication(BKnight, Or(And(AKnight, BKnave),And(AKnave, BKnight))),
    Implication(BKnave,Not(Or(And(AKnight, BKnave),And(AKnave, BKnight))))
)

# Puzzle 3
# A says either "I am a knight." or "I am a knave.", but you don't know which.
# B says "A said 'I am a knave'."
# B says "C is a knave."
# C says "A is a knight."
knowledge3 = And(
    #This is the same as what A says: # A says either "I am a knight." or "I am a knave.", but you don't know which.
    Or(AKnave, AKnight), #A is a knave or a knight
    Not(And(AKnave, AKnight)), #they cannot be both

    Or(BKnave, BKnight), #B is a knave or a knight
    Not(And(BKnave, BKnight)), #they cannot be both

    Or(CKnave, CKnight), #C is a knave or a knight
    Not(And(CKnave, CKnight)), #they cannot be both

    # B says "A said 'I am a knave'."
    # Consider what B says to be P
    # If B is right, then P is true
    # If B lies, P is not true

    # Now, checking P
    # If A is a knave, and he says he is a knave, then he is not a knave
    # P1 = Implication(AKnave, Not(Aknave))
    # If A is a knight, he says the true
    # P2 = Implication *Aknight, Aknave)
    # P = P1 + P2

    Implication(BKnight, And( Implication(AKnave, Not(AKnave)), #P1,
            Implication(AKnight, AKnave) #P2,
    )),

    Implication(BKnave, Not(And( Implication(AKnave, Not(AKnave)), #NOT P - Same as above with not, and BNave
            Implication(AKnight, AKnave)) #P2,
    )),

    Or(And(BKnave, AKnight),And(AKnave, BKnight)), #based on what B says, B and A cannot both be a knight

    Biconditional(CKnave, Not(AKnight)), # C says "A is a knight." | If C is a knave, then A is not a knight; if A is not a knight, C is a knave

    Biconditional(BKnave, Not(CKnave)) # B says "C is a knave."

)

def main():
    symbols = [AKnight, AKnave, BKnight, BKnave, CKnight, CKnave]
    puzzles = [
        ("Puzzle 0", knowledge0),
        ("Puzzle 1", knowledge1),
        ("Puzzle 2", knowledge2),
        ("Puzzle 3", knowledge3)
    ]
    for puzzle, knowledge in puzzles:
        print(puzzle)
        if len(knowledge.conjuncts) == 0:
            print("    Not yet implemented.")
        else:
            for symbol in symbols:
                if model_check(knowledge, symbol):
                    print(f"    {symbol}")


if __name__ == "__main__":
    main()
