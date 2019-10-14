import sys

from preprocessing import trueCreateFeatureVector
from LSTMd import LSTMdef
def filterFun(x):
    if(x != '(' and x != ')' and x!='\n'):
        return(x)


class DeepGen(object):
    def __init__(self):
        self.rules = {}
        self.Operators = []
        self.pop = []
    def generateInitial(self):
        return self.prop 
    def evaluation(self):
        return self.prop 
    def mutation(self):
        return self.prop 
    def cross(self):
        return self.prop
    def test(self):
        return self.prop
    def interpreter(self):
        return self.prop
    def new_gen(self):
        return self.prop


class individual(object):
    def __init__(self):
        self.Operations = []
        self.Metrics = []
        self.testTrain = []
        self.lstmd = None
    def evaluate(self):
        self.Metrics = evaluateModel(self.Operations)    
    def fillOperations(self, operations):
        self.Operations = operations
    def getMetrics(self):
        return self.Metrics
    def getOperations(self):
        return self.Operations

class parser():
    def __init__(self):
        self.rules = './rules/rules'
        self.ruleSet = {}
    def readFile(self):
        f = open(self.rules,'r')
        contentInArchive = f.readlines()
        for i in contentInArchive:
            aux = i.split(' ')
            subR = aux[2].split(',')
            opts = []
            for j in subR:
                preFilter = list(j)
                filtered = filter(filterFun,preFilter)
                operat = ''
                for f in filtered:
                    operat = operat+f
                opts.append(operat) 
            self.ruleSet[aux[0]] = opts


par = parser()
par.readFile() 