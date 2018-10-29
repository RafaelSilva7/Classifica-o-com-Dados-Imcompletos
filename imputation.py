from weka.filters import Filter

class Imputation():
	"""
	Realiza-se a imputação dos dados recebidos como parametros, 
	Atualmente o metodo utilizado é o padrão do WEKA
	data -> weka.dataset.Instances
	"""
	def __init__(self, data):
		self.original_data = data
		self.impute()

	# Realiza a imputação dos dados
	def impute(self):
		filter_imputation = Filter(classname="weka.filters.unsupervised.attribute.ReplaceMissingValues") 
		filter_imputation.inputformat(self.original_data) 
		self.imputed_data = filter_imputation.filter(self.original_data)
		