from imputation import Imputation
from featureSelection import FeatureSelection
from missingPatterns import MissingPatterns
from weka.classifiers import Classifier, Evaluation
from weka.core.classes import Random
from weka.core.dataset import Instances
from myClassifier import MyClassifier

class Training():
	"""
	Núcleo da abordagem, classe responsavel por realizar o treinamento dos classificadores
	por meio da imputação de dados para a seleção das caracteristicas, definindo os padrões ausentes
	para que não seja necessário realizar a imputação dos dados no processo de aplicação

	Parametros:
	data -> weka.core.dataset.Instances
	learn_class = algoritmo de treinamento dos classificadores (String)
	options = configurações do algortimo de treinamento (List)
	"""
	def __init__(self, data, learn_class="weka.classifiers.trees.J48", options=["-C", "0.3"]):
		# Instatinciação das variaveis
		self.data = data # -> weka.core.dataset.Instances
		self.learn_class = learn_class # String
		self.options = options # List
		self.imp = None # Imputation()
		self.selected_features = None # ndarry
		self.missing_patterns = None # ndarry
		self.classifiers = set()
		self.weights = []


	'''
	Realiza o treinamento do conjunto de dados
	'''
	def training(self):
		# Preparação dos dados
		self.imp = Imputation(self.data)

		# Seleciona as caracteristicas
		self.features = FeatureSelection(self.imp.imputed_data)
		data_selected = self.features.data_selected
		self.selected_features = self.features.selected_features

		# Encontra os padrões ausentes
		self.missing_patterns = MissingPatterns(self.data, self.selected_features).missing_patterns

		# Realiza o treinamento dos classificadores
		#print('test train')
		for mpi in self.missing_patterns:

			# Seleciona as caracteristicas
			cpi = set(self.selected_features) - set(mpi)
			data_temp = Instances.copy_instances(data_selected, from_row=0, num_rows=data_selected.num_instances)
			data_temp.class_is_last()

			# Separa os dados de treinamento
			data_temp = self.reduceData(data_temp, cpi, self.data)

			
			# Treina os classificadores com os dados imputados
			classifier = Classifier(classname=self.learn_class, options=self.options)
			classifier.build_classifier(data_temp)
			
			#print(classifier.distribution_for_instance(data_selected.get_instance(30)))
			

			#!!!!!! Verica o peso de cada classificador (sua acuracia de classificação)
			evl = Evaluation(data_temp)
			evl.crossvalidate_model(classifier, data_temp, 15, Random(1))

			# Adiciona os classificadores treinados ao conjunto de classificadores
			my_classifier = MyClassifier(classifier, cpi, 1 - evl.mean_absolute_error)
			self.classifiers.add(my_classifier)

		#print(data_temp.class_attribute)
		#print("\n---------------------------------------\n")


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