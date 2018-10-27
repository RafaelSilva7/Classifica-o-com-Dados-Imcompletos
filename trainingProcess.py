from imputation import Imputation
from featureSelection import FeatureSelection
from missingPatterns import MissingPatterns


class Training():
	"""
	Núcleo da abordagem, classe responsavel por realizar o treinamento dos classificadores
	por meio da imputação de dados para a seleção das caracteristicas, definindo os padrões ausentes
	para que não seja necessário realizar a imputação dos dados no processo de aplicação

	Parametros:
	data = conjunto de dados a serem classificados
	learn_class = algoritmo de treinamento dos classificadores
	"""
	def __init__(self, data, learn_class):
		# Instatinciação das variaveis
		self.data = data
		self.learn_class = learn_class
		self.imp_data = None
		self.selected_feature = None
		self.missing_patterns = None
		self.classifiers = []
		self.weights = []

		# Execução do treinamento
		self.execute()


	def execute(self):
		# Preparação dos dados
		self.imp_data = Imputation(data)
		self.selected_feature = FeatureSelection(imp_data)

		# Encontra os padrões ausentes
		data_selected = self.data.SelectFeature(selected_feature)
		self.missing_patterns = MissingPatterns(data_selected)

		# Realiza o treinamento dos classificadores
		for mpi in missing_patterns:
			# Seleciona as caracteristicas
			classifier_pattern = selected_feature.intersection(mpi)

			# Separa o conjunto de dados para o treinamento e validação
			imp_train = imp_data.SelectData(classifier_pattern)
			imp_validation = imp_data.data_class()

			# Treina os classificadores com os dados imputados
			classifier = self.learn_class.learn()
			self.classifiers.append(classifier)

			# Verica o peso de cada classificador (sua acuracia de classificação)
			weight = classifier.validation(imp_validation)
			self.weights.append(weight)

		return (classifiers, weights, selected_feature)


