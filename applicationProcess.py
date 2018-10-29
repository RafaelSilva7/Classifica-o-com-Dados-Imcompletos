from weka.core.dataset import Instances
from weka.classifiers import Classifier
from myClassifier import MyClassifier
import numpy as np

class ApplicationProcess():
	"""
	Realiza o processo de aplicação do algoritmo, ou seja, realiza a classificação de novas
	instancias com base nos classificadores já treinados
	instance -> weka.core.dataset.Instance
	selected_features -> set()
	classifiers -> MyClassifier (classificador desenvolvido para o algortimo)
	"""
	def __init__(self, instance, selected_features, classifiers):
		self.instance = instance # -> weka.core.dataset.Instance
		self.selected_features = selected_features # -> set()
		self.classifiers = [] # -> MyClassifier (classificador desenvolvido para o algortimo)
		self.rate_distrib = None
		for cls in classifiers:
			temp = MyClassifier(Classifier.make_copy(cls.classifier), cls.features, cls.weight)
			self.classifiers.append(temp)


	"""
	Função que realiza a classificação de uma nova instancia com base nos parametros
	definidos durante a instanciação do objeto ApplicationProcess
	"""
	def applicationProcess(self):
		# Verifica se a instancia possui missing values
		if self.instance.has_missing():
			for i in range(0,self.instance.num_attributes):
				if self.instance.is_missing(i):
					# Parar cada missing values, verifica os classificadores a serem usados
					for classifier in self.classifiers:
						if i in classifier.features:
							self.classifiers.remove(classifier)

		list_distrib = []
		#print("Distribuição da instancia classificada (sem os pesos):")
		for cls in self.classifiers:
			distrib = cls.classifier.distribution_for_instance(self.instance)
			#print(distrib, cls.weight)
			for i in range(0, self.instance.num_classes):
				distrib[i] *= cls.weight
			list_distrib.append(distrib)

		#print("\nDistribuição da instancia classificada (com os pesos):")
		#for d in list_distrib:
		#	print(d)

		self.rate_distrib = np.ndarray((self.instance.num_classes,))
		for i in range(0, self.instance.num_classes):
			rate = 0
			for distrib in list_distrib:
				rate += distrib[i]

			rate /= self.instance.num_classes
			self.rate_distrib[i] = rate







	'''
	Realiza a redução de um conjunto de instancias, segunda as caracteristicas informadas
	data -> weka.core.dataset.Instances
	features -> set()
	original_data -> weka.core.dataset.Instances
	'''
	def reduceData(self, data, features, original_data):
		i = 0;
		while i < data.num_attributes:
			flag = True
			for j in features:
				if str(original_data.attribute(j)) == str(data.attribute(i)):
					flag = False
					pass

			if flag:
				data.delete_attribute(i)
			else:
				i += 1
		return data	