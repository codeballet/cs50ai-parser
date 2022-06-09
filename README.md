# Parser

## Introduction

Parser is an AI that parse sentences and extract noun phrases.

Parsing sentences is a common task in natural language processing, aiming to understand the structure and meaning of a sentence. In particular, extracting noun phrases may help to gain an understanding of what a sentence is about.

The AI Parser of this project uses the concept of 'context-free grammar formalism' to parse English sentences and determine their structure. The Python library used for the language processing is [NLTK (Natural Language Toolkit)](https://www.nltk.org/index.html).

## Context-free grammar

In a context-free grammar, we repeatedly apply rewriting rules to transform symbols into other symbols. The objective is to start with a nonterminal symbol `S` (representing a sentence) and repeatedly apply context-free grammar rules until we generate a complete sentence of terminal symbols (i.e., words). The rule `S -> N V`, for example, means that the `S` symbol can be rewritten as `N V` (a noun followed by a verb). If we also have the rule `N -> "Holmes"` and the rule `V -> "sat"`, we can generate the complete sentence `"Holmes sat."`.

Of course, noun phrases might not always be as simple as a single word like `"Holmes"`. We might have noun phrases like `"my companion"` or `"a country walk"` or `"the day before Thursday"`, which require more complex rules to account for. To account for the phrase `"my companion"`, for example, we might imagine a rule like:

```
NP -> N | Det N
```

In this rule, we say that an `NP` (a “noun phrase”) could be either just a noun (`N`) or a determiner (`Det`) followed by a noun, where determiners include words like `"a"`, `"the"`, and `"my"`. The vertical bar (`|`) just indicates that there are multiple possible ways to rewrite an `NP`, with each possible rewrite separated by a bar.

## Defining a "noun phrase chunk"

For this project, a “noun phrase chunk” is defined as a noun phrase that doesn’t contain other noun phrases within it. Put more formally, a noun phrase chunk is a subtree of the original tree whose label is NP and that does not itself contain other noun phrases as subtrees.

For example, if `"the home"` is a noun phrase chunk, then `"the armchair in the home"` is not a noun phrase chunk, because the latter contains the former as a subtree.

## Limitations and expansion of the AI's capabilities

As may be seen in the code, the project currently contains an extremely small collection of words, stored in the `TERMINALS` variable. Moreover, the collection of context-free grammar rules is also very limited, stored in the `NONTERMINALS` variable.

The collections of `TERMINALS` and `NONTERMINALS` is just about big enough to parse the sentences provided in the project, stored as a collection of files in the `./sentences/` directory. In case you would like to parse other sentences, please do expand the content of the `TERMINALS` and the `NONTERMINALS` variables.

## Intellectual Property Rights

MIT

## Acknowledgements

The project was created as part of Harvard's course CS50 Introduction to Artificial Intelligence with Python.
