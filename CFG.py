import nltk


class CFGParser:
    def __init__(self):
        self.parser = nltk.FeatureEarleyChartParser(nltk.load('feature_grammars/feat0.fcfg'))
        self.tokens = None

    def print_trees(self, tokens):
        self.tokens = tokens
        printParsedTrees(self.parser, self.tokens)


# if there are any trees found, print them
def printParsedTrees(parser, tokens):
    print("********** parse tree **********")
    i = 0
    for tree in parser.parse(tokens):
        i = i+1
        if i is 1:
            print(tree)
    print("num trees: {}".format(i))

