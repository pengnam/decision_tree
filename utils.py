from model import (Leaf, DecisionNode, Question, class_counts)

###########################
#### Utility Functions ####
###########################
def print_tree(node, spacing=""):
    if isinstance(node, Leaf):
        print(spacing + "Predict", node.predictions)

    # Base case: we've reached a leaf
    if isinstance(node, Leaf):
        print (spacing + "Predict", node.predictions)
        return

    # Print the question at this node
    print (spacing + str(node.question))

    # Call this function recursively on the true branch
    print (spacing + '--> True:')
    print_tree(node.true_branch, spacing + "  ")

    # Call this function recursively on the false branch
    print (spacing + '--> False:')
    print_tree(node.false_branch, spacing + "  ")

def print_results(counts):
    total = float(sum(counts.values()))
    probs = {}
    for lbl in counts.keys():
        probs[lbl] = str(int(counts[lbl] / total * 100)) + "%"
    return probs

def build_tree(rows):
    """
        Builds tree from given rows
    """
    gain, question = find_best_split(rows)

    if gain == 0:
        return Leaf(rows)

    true_rows, false_rows = question.partition(rows)
    true_branch = build_tree(true_rows)
    false_branch = build_tree(false_rows)

    return DecisionNode(question, true_branch, false_branch)
######################
## Helper Functions ##
######################
def find_best_split(rows):
    best_gain = 0
    best_question = None
    current_uncertainty = gini(rows)
    n_features = len(rows[0]) - 1

    for col in range(n_features):
        values = set([row[col] for row in rows])
        for val in values:
            question = Question(col, val)

            true_rows, false_rows = question.partition(rows)
            if len(true_rows) == 0 or len(false_rows) == 0:
                continue
            gain = info_gain(true_rows, false_rows, current_uncertainty)
            if gain >= best_gain:
                best_gain = gain
                best_question = question
    return best_gain, best_question

def info_gain(left, right, current_uncertainty):
    """ Information gain

    The uncertainty of the starting node minus the weighted impurity of the two child nodes

    Args:
        left (list): list of rows
        right (list): list of rows
        current_uncertainty (float): current uncertainty value of the root node.
    Returns:
        gain (float): the gain in uncertainty value

    """
    p = float(len(left))/ float(len(left)+ len(right))
    return current_uncertainty - p * gini(left) - (1 - p) * gini(right)

def gini(rows):
    """Gini impurity calculation

    Measure of how often a randomly chosen element from the set would be incorrectly labelled if it was randomly labeled according to the distribution of labels i the subset. (https://en.wikipedia.org/wiki/Decision_tree_learning#Gini_impurity)

    Args:
        rows (list): list of rows
    Returns:
        impurity (float): impurity value
    """
    counts = class_counts(rows)
    impurity = 1
    for lbl in counts:
        prob_of_lbl = counts[lbl] / float(len(rows))
        impurity -= prob_of_lbl ** 2

    return impurity

