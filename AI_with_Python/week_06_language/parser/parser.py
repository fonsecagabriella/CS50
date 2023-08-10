import nltk
import sys

TERMINALS = """
Adj -> "country" | "dreadful" | "enigmatical" | "little" | "moist" | "red"
Adv -> "down" | "here" | "never"
Conj -> "and" | "until"
Det -> "a" | "an" | "his" | "my" | "the"
N -> "armchair" | "companion" | "day" | "door" | "hand" | "he" | "himself"
N -> "holmes" | "home" | "i" | "mess" | "paint" | "palm" | "pipe" | "she"
N -> "smile" | "thursday" | "walk" | "we" | "word"
P -> "at" | "before" | "in" | "of" | "on" | "to"
V -> "arrived" | "came" | "chuckled" | "had" | "lit" | "said" | "sat"
V -> "smiled" | "tell" | "were"
"""

NONTERMINALS = """
S -> VP | NP | AdjP
VP -> V | NP VP | VP NP | NP V NP | VP Conj VP | VP Adv
NP -> N | Det N | Det AdjP | P NP | NP Adv | NP NP
AdjP -> Adj | AdjP N | P AdjP | Adj AdjP

"""

grammar = nltk.CFG.fromstring(NONTERMINALS + TERMINALS)
parser = nltk.ChartParser(grammar)


def main():

    # If filename specified, read sentence from file
    if len(sys.argv) == 2:
        with open(sys.argv[1]) as f:
            s = f.read()

    # Otherwise, get sentence as input
    else:
        s = input("Sentence: ")

    # Convert input into list of words
    s = preprocess(s)

    # Attempt to parse sentence
    try:
        trees = list(parser.parse(s))
    except ValueError as e:
        print(e)
        return
    if not trees:
        print("Could not parse sentence.")
        return

    # Print each tree with noun phrase chunks
    for tree in trees:
        tree.pretty_print()

        print("Noun Phrase Chunks")
        for np in np_chunk(tree):
            print(" ".join(np.flatten()))


def preprocess(sentence):
    """
    Convert `sentence` to a list of its words.
    Pre-process sentence by converting all characters to lowercase
    and removing any word that does not contain at least one alphabetic
    character.
    """

    words =  nltk.word_tokenize(sentence.lower()) # convert sentence to lower case and split it to list of words using tokenize

    #remove any word that does not contain at least one alphabetic character
    for w in words:
        if not any(char.isalpha() for char in w):
            words.remove(w)

    return words



def np_chunk(tree):
    """
    Return a list of all noun phrase chunks in the sentence tree.
    A noun phrase chunk is defined as any subtree of the sentence
    whose label is "NP" that does not itself contain any other
    noun phrases as subtrees.
    """

    # list of chuncks to return
    chuncks = []

    #print ("SUB TREES")
    #print (tree.subtrees())

    for st in tree.subtrees(): # for each subtree in given tree
        #print (f"LABEL: {st.label()}")
        #print ("CHILDREN:")
        #for child in st:
        #    print (child.label())

        # if the label of the subtree is NP and
        # this subtreee has no child with label of NP, adds to the list to return
        if st.label() == "NP" and not any(child.label() == "NP" for child in st):
            chuncks.append(st)

    return chuncks



if __name__ == "__main__":
    main()
