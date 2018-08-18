

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
    def classify(self, row):
        if self.question.match(row):
            return self.true_branch.classify(row)
        else:
            return self.false_branch.classify(row)


class Leaf:
    def __init__(self, rows):
        self.predictions = class_counts(rows)
    def classify(self, row):
        return self.predictions

class Question:
    def __init__(self, column, value):
        self.column = column
        self.value = value
    def partition(self, rows):
        true_rows, false_rows = [], []
        for row in rows:
            if self.match(row):
                true_rows.append(row)
            else:
                false_rows.append(row)
        return true_rows, false_rows

    def match(self, example):
        return example[self.column] >= self.value

    def __repr__(self):
        return "{0} value >= {1}".format(self.column, self.value)





