# análisis de datos 
import numpy
import math
#import matplotlib



class analisisResults :
	arregloResultadosObtenidos = []
	arregloResultadosEsperados = []

	def __init__ (self , val1 , val2 ) :
		self.arregloResultadosObtenidos = val1 
		self.arregloResultadosEsperados = val2

	def testAccuracy (self) :
		possitiveCases = 0
		for i in range(0 , len(self.arregloResultadosEsperados)) :
			if (self.arregloResultadosObtenidos [i] == self.arregloResultadosEsperados[i]) :
				possitiveCases += 1
		accuracy = possitiveCases / len(self.arregloResultadosEsperados)
		return accuracy
	def testPresicion (self) :
		falsPossitive = 0
		truePossitive = 0
		pres = 0
		for i in range (len(self.arregloResultadosEsperados)) :
			if (self.arregloResultadosObtenidos[i] == 1 and self.arregloResultadosEsperados[i] == 0) :
				falsPossitive += 1
			if (self.arregloResultadosObtenidos[i] == 0 and self.arregloResultadosEsperados[i] == 1) :
				falsPossitive += 1
			if (self.arregloResultadosEsperados[i] == self.arregloResultadosEsperados[i]) :
				truePossitive += 1
		#print(truePossitive)
		#print(falsPossitive)
		if(truePossitive > 0) :
			pres = (truePossitive/(truePossitive+falsPossitive))
		return pres

	
	def testSpecificity (self) :
		truePos = 0
		FalseNegative = 0
		for i in range (len(self.arregloResultadosEsperados)) :
			if (self.arregloResultadosEsperados[i] == 1 and self.arregloResultadosObtenidos[i]==1) :
				#print ("T")
				truePos += 1
			if (self.arregloResultadosEsperados[i] == 1 and self.arregloResultadosObtenidos[i]==0) :
				FalseNegative += 1
		Sensitivity = truePos/(truePos + FalseNegative)

		return Sensitivity
	def testSensitivity (self) :
		trueNeg = 0
		falseNeg = 0
		for i in range (len(self.arregloResultadosEsperados)) :
			if (self.arregloResultadosEsperados[i] == 0 and self.arregloResultadosObtenidos[i]==0) :
				trueNeg += 1
			if (self.arregloResultadosEsperados[i] == 0 and self.arregloResultadosObtenidos[i]==1) :
				falseNeg += 1
		Specificity = trueNeg/(trueNeg+falseNeg)
		return Specificity
	def MattCorr (self) :
		trueNeg = 0
		truePos = 0
		falsNeg = 0
		falsPos = 0
		for i in range (len(self.arregloResultadosEsperados)) :
			if (self.arregloResultadosEsperados[i] == 0 and self.arregloResultadosObtenidos[i]==0) :
				trueNeg += 1
			if (self.arregloResultadosEsperados[i] == 0 and self.arregloResultadosObtenidos[i]==1) :
				falsNeg += 1
			if (self.arregloResultadosEsperados[i] == 1 and self.arregloResultadosObtenidos[i]==1) :
				#print ("T")
				truePos += 1
			if (self.arregloResultadosObtenidos[i] == 1 and self.arregloResultadosEsperados[i] == 0) :
				falsPos += 1
		MCC = (truePos*trueNeg - falsPos*falsNeg)/(math.sqrt((truePos+falsPos)*(truePos+falsNeg)*(trueNeg+falsPos)*(trueNeg+falsNeg)))
		return MCC
