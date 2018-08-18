

#######################
## Utility functions ##
#######################
def class_counts(rows):
    count = {}
    for row in rows:
        label = row[-1]
        if label not in count:
            count [label] = 1
        else:
            count[label] += 1
    return count

##############
### Models ###
##############
class DecisionNode:
    def __init__(self, question, true_branch, false_branch):
        self.question = question
        self.true_branch = true_branch
        self.false_branch = false_branch

    def build_tree(rows):

    def print_tree(node, spacing=""):

    def classify(row, node):

    def print_leaf(counts):

def Leaf:
    def __init__(self, rows):

