class Node:

    def __init__(self, node = None):
        if node is None:
            self.ctor()
        else:
            self.cctor(node)

    def ctor(self):
        self.status = [0 for i in range(5)]      # <_, _, _, _, _> || 0 if on source, 1 if on dest
        self.time = 0                           # total time passed
        self.prevPath = []                      # array of Node

    def cctor(self, node):
        self.status = []
        self.time = node.time
        self.prevPath = []
        for i in range(5):
            self.status.append(node.status[i])
        for i in range(len(node.prevPath)):
            self.prevPath.append(node.prevPath[i])
        #self.prevPath.append(node)                         # to print transition 

    # Get value

    def getTime(self):
        return self.time

    def get0Idx(self):
        idx = []
        for i in range(5):
            if self.status[i] == 0:
                idx.append(i)
        return idx

    def isSolution(self):
        solution = True
        for i in range(len(self.status)):
            if self.status[i] == 0:
                solution = False
                break
        return solution

    # Set value

    def setMinimumTo0(self):
        for i in range(len(self.status)):
            if self.status[i] == 1:
                self.status[i] = 0
                self.addTime(i)
                break

    def setTo1(self, xi, xj):
        self.status[xi] = 1
        self.status[xj] = 1
        self.addTime(xj)

    def addTime(self, x):
        if x == 0:
            self.time += 1
        elif x == 1:
            self.time += 3
        elif x == 2:
            self.time += 6
        elif x == 3:
            self.time += 8
        elif x == 4:
            self.time += 12

    # Printer

    def printNode(self):
        print(self.status, end = ", ")

    def printPrevPath(self):
        # self.prevPath.append(self)
        for i in range(len(self.prevPath)):
            print("Langkah ke-"+str(i+1)+":")
            self.prevPath[i].printNode()
            print(self.prevPath[i].getTime())           # for each node time
        print(self.time)
        print("="*10)

    # Add path

    def addPath(self, other):
        newNode = Node(other)
        self.prevPath.append(newNode)

    