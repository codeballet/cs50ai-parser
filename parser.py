import nltk
import sys
from nltk.tokenize import word_tokenize

# uncomment below line if 'punkt' not downloaded
# nltk.download('punkt')

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
S -> NP | NP VP | S Conj S
NP -> N | Det N | NP PP | Det AP N
VP -> V | V NP | V PP | NP V | VP Conj VP | Adv VP | V PP Adv | VP Adv
PP -> P | P NP
AP -> Adj | Adj Adj | Adj Adj Adj
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

    # experimenting with tree label function
    print(trees)
    print("\nLabels:")
    print(trees[0])
    print(trees[0].label())
    print(trees[0][0])
    print(trees[0][0].label())

    # experimenting with tree subtrees function
    print("\nSubtrees:")
    for something in trees[0].subtrees():
        print(something)
        print(something.label())

    print('\nOnly NP phrases')
    for e in trees[0].subtrees(lambda e: e.label() == 'NP'):
        print(e)

    print(f'\nHeight of tree: {trees[0].height()}')
    t = trees[0]
    for e in trees[0].subtrees(lambda t: t.height() == 4):
        print(f'\nheight: {e.height()}')
        print(e)
    for e in trees[0].subtrees(lambda t: t.height() == 3):
        print(f'height: {e.height()}')
        print(e)
    for e in trees[0].subtrees(lambda t: t.height() == 2):
        print(f'height: {e.height()}')
        print(e)

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
    words = [
        word.lower() for word in 
        word_tokenize(sentence)
        if any(c.isalpha() for c in word)
    ]
    
    return words


def np_chunk(tree):
    """
    Return a list of all noun phrase chunks in the sentence tree.
    A noun phrase chunk is defined as any subtree of the sentence
    whose label is "NP" that does not itself contain any other
    noun phrases as subtrees.
    """
    # Get all NPs
    nps_all = list()
    for e in tree.subtrees(lambda e: e.label() == 'NP'):
        print(e)
        nps_all.append(e)
    print()

    # Get NPs that contain other NPs inside them
    nps_remove = list()
    for np1 in nps_all:
        for np2 in nps_all:
            if np2 != np1:
                if np2.height() > np1.height() and np1 in np2:
                    nps_remove.append(np2)

    # Remove all NPs containing other NPs inside them
    nps_chunks = list(filter(lambda i: i not in nps_remove, nps_all))

    return nps_chunks


if __name__ == "__main__":
    main()
