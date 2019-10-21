import sys
import random
import math

from preprocessing import trueCreateFeatureVector
from LSTMd import LSTMdef
def filterFun(x):
    if(x != '(' and x != ')' and x!='\n'):
        return(x)
def evaluateModel(operations,metrics):
    model = LSTMdef(operations[0],operations[1],operations[2],operations[3],operations[4],operations[5],operations[6],operations[7],operations[8],operations[9],operations[10])
    model.generate()
    resl = model.test()
    accuracy = resl.testAccuracy()
    presicion = resl.testPresicion()
    sensitivity = resl.testSensitivity()
    specificity = resl.testSpecificity()
    mattcorr = resl.MattCorr()
    f1 = 2*((presicion*sensitivity)/(sensitivity+presicion))
    with open("resl.csv", "a") as f:
        f.write(str(operations[0])+','+str(operations[1])+','+str(operations[2])+','+str(operations[3])+','+str(operations[4])+','+str(operations[5])+','+str(operations[6])+','+str(operations[7])+','+str(operations[8])+','+str(operations[9])+','+str(operations[10])+','+str(accuracy)+','+str(presicion)+','+str(sensitivity)+','+str(specificity)+','+str(mattcorr)+','+str(f1)+'\n')
    return[accuracy,presicion,sensitivity,specificity,mattcorr,f1]

class DeepGen(object):
    def __init__(self):
        par = parser()
        self.rules = par.readFile()
        self.Operators = []
        self.pop = []
        self.quantity = 10
        self.metrics = [0.5,0.5,0,0.5,0,0.5]
        with open("resl.csv","w") as f:
            f.write("rangeL"+','+"rangeC"+','+"dropC"+','+"rdropC"+','+"react"+','+"optim"+','+"loss"+','+"batchC"+','+"learningCh"+','+"amsgrad"+','+"epochC"+','+"accuracy"+','+"presicion"+','+"sensitivity"+','+"specificity"+','+"mattcorr"+','+"f1"+'\n')
    def generateInitial(self):
        lstmR = self.rules['rangeLayLstm']
        celR = self.rules['rangeLstm']
        optimR = self.rules['optim']
        lossR = self.rules['loss']
        rAct = self.rules['ractivation']
        batchR = self.rules['batch'] 
        learningRater = self.rules['learningRate']
        dropR = self.rules['drop']
        rdropR = self.rules['rdrop']
        epochr = self.rules['epochs']
        for i in range(0,self.quantity):
            ind = individual(self.metrics)
            rangeL = math.ceil(random.randrange(int(lstmR[0]),int(lstmR[1])))         
            rangeC = math.ceil(random.randrange(int(celR[0]),int(celR[1])))
            optimChoos = math.ceil(random.randrange(0,len(optimR)-1))
            optim = optimR[optimChoos]
            lossChoos = math.ceil(random.randrange(0,len(lossR)-1))
            loss = lossR[lossChoos]
            rActc = math.ceil(random.randrange(0,len(rAct)-1))
            react = rAct[rActc]
            batchC = math.ceil(random.randrange(int(batchR[0]),int(batchR[1])))
            dropC = random.uniform(float(dropR[0]),float(dropR[1]))
            rdropC = random.uniform(float(rdropR[0]),float(rdropR[1]))
            epochC = math.ceil(random.randrange(int(epochr[0]),int(epochr[1])))
            amsgrad = False
            if(optim == 'adam'):
                prob = random.random()
                if(prob > 0.5):
                    amsgrad = True
            learningCh = random.uniform(float(learningRater[0]),float(learningRater[1]))
            operationsl = [rangeL,rangeC,dropC,rdropC,react,optim,loss,batchC,learningCh,amsgrad,epochC]
            ind.fillOperations(operationsl)
            self.pop.append(ind) 
    def evaluation(self):
        ans = []
        aux = []
        for i in self.pop:
            ans.append(i.evaluate(self.metrics))
        for i in range(0,len(ans)):
            if(ans[i]>0.5):
                aux.append(self.pop[i])
            if(ans[i]==0.5):
                b = random.randint(0,1)
                if(b==1):
                    aux.append(self.pop[i])
        self.pop = aux
    def mutation(self):
        lstmR = self.rules['rangeLayLstm']
        celR = self.rules['rangeLstm']
        optimR = self.rules['optim']
        lossR = self.rules['loss']
        rAct = self.rules['ractivation']
        batchR = self.rules['batch'] 
        learningRater = self.rules['learningRate']
        dropR = self.rules['drop']
        rdropR = self.rules['rdrop']
        epochr = self.rules['epochs']
        for i in self.pop:
            mut = random.randint(0,100)
            chooser = random.randint(0,11)
            if(mut > 70):
                if(chooser == 1):
                    rangeL = math.ceil(random.randrange(int(lstmR[0]),int(lstmR[1])))
                    i.Operations[0] = rangeL
                if(chooser == 2):
                    rangeC = math.ceil(random.randrange(int(celR[0]),int(celR[1])))
                    i.Operations[1] = rangeC
                if(chooser == 3):
                    dropC = random.uniform(float(dropR[0]),float(dropR[1]))
                    i.Operations[2] = dropC
                if(chooser == 4):
                    rdropC = random.uniform(float(rdropR[0]),float(rdropR[1]))
                    i.Operations[3] = rdropC
                if(chooser == 5):
                    rActc = math.ceil(random.randrange(0,len(rAct)-1))
                    react = rAct[rActc]
                    i.Operations[4] = react
                if(chooser == 6):
                    optimChoos = math.ceil(random.randrange(0,len(optimR)-1))
                    optim = optimR[optimChoos]
                    i.operations[5] = optim 
                if(chooser == 7):
                    lossChoos = math.ceil(random.randrange(0,len(lossR)-1))
                    loss = lossR[lossChoos]
                    i.operations[6] = loss 
                if(chooser == 8):
                    batchC = math.ceil(random.randrange(int(batchR[0]),int(batchR[1])))
                    i.operations[7] = batchC
                if(chooser == 9):
                    learningCh = random.uniform(float(learningRater[0]),float(learningRater[1]))
                    i.operations[8] = learningCh
                if(chooser == 11):
                    epochC = math.ceil(random.randrange(int(epochr[0]),int(epochr[1])))
                    i.operations[11] = epochC
    def cross(self):
            for j in range(0,len(self.pop)-1):
                aux = []
                aux.append(self.pop[j].getOperations()[0:5]+self.pop[j+1].getOperations()[6:10])
                self.pop[j].operations = aux
    def new_gen(self):
        lstmR = self.rules['rangeLayLstm']
        celR = self.rules['rangeLstm']
        optimR = self.rules['optim']
        lossR = self.rules['loss']
        rAct = self.rules['ractivation']
        batchR = self.rules['batch'] 
        learningRater = self.rules['learningRate']
        dropR = self.rules['drop']
        rdropR = self.rules['rdrop']
        epochr = self.rules['epochs']
        actual = len(self.pop)
        needed = self.quantity - actual
        print(needed)
        for i in range(0,needed):
            ind = individual(self.metrics)
            rangeL = math.ceil(random.randrange(int(lstmR[0]),int(lstmR[1])))         
            rangeC = math.ceil(random.randrange(int(celR[0]),int(celR[1])))
            optimChoos = math.ceil(random.randrange(0,len(optimR)-1))
            optim = optimR[optimChoos]
            lossChoos = math.ceil(random.randrange(0,len(lossR)-1))
            loss = lossR[lossChoos]
            rActc = math.ceil(random.randrange(0,len(rAct)-1))
            react = rAct[rActc]
            batchC = math.ceil(random.randrange(int(batchR[0]),int(batchR[1])))
            dropC = random.uniform(float(dropR[0]),float(dropR[1]))
            rdropC = random.uniform(float(rdropR[0]),float(rdropR[1]))
            epochC = math.ceil(random.randrange(int(epochr[0]),int(epochr[1])))
            amsgrad = False
            if(optim == 'adam'):
                prob = random.random()
                if(prob > 0.5):
                    amsgrad = True
            learningCh = random.uniform(float(learningRater[0]),float(learningRater[1]))
            operationsl = [rangeL,rangeC,dropC,rdropC,react,optim,loss,batchC,learningCh,amsgrad,epochC]
            ind.fillOperations(operationsl)
            self.pop.append(ind)
    def genetic(self):
        self.generateInitial()
        generation = 1
        while sum(self.metrics)<4.75:
            print("generation : "+str(generation))
            self.evaluation()
            self.medEstablish()
            self.cross()
            self.mutation()
            self.new_gen()
            generation = generation + 1
    def medEstablish(self):
        vals = []
        num = len(self.pop)
        print(num)
        for i in self.pop:
            if(vals != []):
                #print(i.getMetrics())
                vals[0] = [vals[0][0]+i.getMetrics()[0],vals[0][1]+i.getMetrics()[1],vals[0][2]+i.getMetrics()[2],vals[0][3]+i.getMetrics()[3],vals[0][4]+i.getMetrics()[4],vals[0][5]+i.getMetrics()[5] ]
            else:
                #print(i.getMetrics())
                vals.append(i.getMetrics())
        print(vals)
        meds = [vals[0][0]/num,vals[0][1]/num,vals[0][2]/num,vals[0][3]/num,vals[0][4]/num,vals[0][5]/num] 
        self.metrics = meds



class individual(object):
    def __init__(self, metrics):
        self.Operations = []
        self.Metrics = metrics
        self.testTrain = []
        self.lstmd = None
        self.metrics = [] 
    def evaluate(self,metrics):
        self.metrics = evaluateModel(self.Operations,metrics)
        #print(self.metrics)
        total = self.metrics[0]+self.metrics[1]+self.metrics[2]+self.metrics[3]+self.metrics[4]+self.metrics[5]
        med = sum(metrics)
        if(total > med):
            return 1
        elif(total == med):
            return 0.5
        else:
            return 0   
    def fillOperations(self, operations):
        self.Operations = operations
    def getMetrics(self):
        return self.metrics
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
        return(self.ruleSet)


gen = DeepGen()
gen.genetic()