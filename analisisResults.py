# análisis de datos 
import numpy
import math
#import matplotlib



class analisisResults :
	arregloResultadosObtenidos = []
	arregloResultadosEsperados = []

	def __init__ (Self , val1 , val2 ) :
		Self.arregloResultadosObtenidos = val1 
		Self.arregloResultadosEsperados = val2

	def testAccuracy (Self) :
		possitiveCases = 0
		for i in range(0 , len(Self.arregloResultadosEsperados)) :
			if (Self.arregloResultadosObtenidos [i] == Self.arregloResultadosEsperados[i]) :
				possitiveCases += 1
		accuracy = possitiveCases / len(Self.arregloResultadosEsperados) * 100
		return accuracy
	def testPresicion (Self) :
		falsPossitive = 0
		truePossitive = 0
		pres = 0
		for i in range (len(Self.arregloResultadosEsperados)) :
			if (Self.arregloResultadosObtenidos[i] == 1 and Self.arregloResultadosEsperados[i] == 0) :
				falsPossitive += 1
			if (Self.arregloResultadosObtenidos[i] == 0 and Self.arregloResultadosEsperados[i] == 1) :
				falsPossitive += 1
			if (Self.arregloResultadosEsperados[i] == Self.arregloResultadosEsperados[i]) :
				truePossitive += 1
		#print(truePossitive)
		#print(falsPossitive)
		if(truePossitive > 0) :
			pres = (truePossitive/(truePossitive+falsPossitive))*100
		return pres

	
	def testSpecificity (Self) :
		truePos = 0
		FalseNegative = 0
		for i in range (len(Self.arregloResultadosEsperados)) :
			if (Self.arregloResultadosEsperados[i] == 1 and Self.arregloResultadosObtenidos[i]==1) :
				#print ("T")
				truePos += 1
			if (Self.arregloResultadosEsperados[i] == 1 and Self.arregloResultadosObtenidos[i]==0) :
				FalseNegative += 1
		Sensitivity = truePos/(truePos + FalseNegative)*100

		return Sensitivity
	def testSensitivity (Self) :
		trueNeg = 0
		falseNeg = 0
		for i in range (len(Self.arregloResultadosEsperados)) :
			if (Self.arregloResultadosEsperados[i] == 0 and Self.arregloResultadosObtenidos[i]==0) :
				trueNeg += 1
			if (Self.arregloResultadosEsperados[i] == 0 and Self.arregloResultadosObtenidos[i]==1) :
				falseNeg += 1
		Specificity = trueNeg/(trueNeg+falseNeg)*100
		return Specificity
	def MattCorr (Self) :
		trueNeg = 0
		truePos = 0
		falsNeg = 0
		falsPos = 0
		for i in range (len(Self.arregloResultadosEsperados)) :
			if (Self.arregloResultadosEsperados[i] == 0 and Self.arregloResultadosObtenidos[i]==0) :
				trueNeg += 1
			if (Self.arregloResultadosEsperados[i] == 0 and Self.arregloResultadosObtenidos[i]==1) :
				falsNeg += 1
			if (Self.arregloResultadosEsperados[i] == 1 and Self.arregloResultadosObtenidos[i]==1) :
				#print ("T")
				truePos += 1
			if (Self.arregloResultadosObtenidos[i] == 1 and Self.arregloResultadosEsperados[i] == 0) :
				falsPos += 1
		MCC = (truePos*trueNeg - falsPos*falsNeg)/(math.sqrt((truePos+falsPos)*(truePos+falsNeg)*(trueNeg+falsPos)*(trueNeg+falsNeg)))
		return MCC*100
