from Node import Node
import itertools

def backtrack(node):
    if node.getTime() <= 30:
        if node.isSolution():
            node.printPrevPath()
        else:
            node.setMinimumTo0()
            # combinations
            zeroIdx = node.get0Idx()
            idx = []
            for subset in itertools.combinations(zeroIdx, 2):
                idx.append(subset)
            # foreach combination, set to 1, call backtrack(that node)
            for i in idx:
                newNode = Node(node)
                newNode.setTo1(i[0], i[1])
                newNode.addPath(newNode)
                backtrack(newNode)
    # else: # to print backtracked
    #     node.printPrevPath()

if __name__ == "__main__":
    root = Node()
    backtrack(root)