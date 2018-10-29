class MissingPatterns():
	"""docstring for MissingPatterns"""
	def __init__(self, data, selected_features):
		self.missing_patterns = set() # -> set de frozenset
		self.data = data # -> weka.core.dataset.Instances
		self.missingPatterns(selected_features);

	# Encontra os padrões ausentes
	def missingPatterns(self, selected_features):
		for instance in self.data: #instance -> weka.core.dataset.Instance
			temp = set()

			#Verfica o padrão ausente de cada instancia
			for j in range(0, self.data.num_attributes):
				for i in selected_features:
					if str(self.data.attribute(j)) == str(self.data.attribute(i)):
						if instance.is_missing(j):
							temp.add(j)

			#E realiza sua adição ao conjunto de padrões ausentes
			self.missing_patterns.add(frozenset(temp))