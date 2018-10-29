
class MyClassifier():
	"""docstring for MyClassifier"""
	def __init__(self, classifier=None, features=None, weight=None):
		self.classifier = classifier # -> weka.classifiers.Classifier
		self.features = features # -> set()
		self.weight = weight
		self.distribuition = None # -> ndarray


	def set_features(self, features):
		self.features = features


	def set_classifier(self, classifier):
		self.classifier = classifier
		

	def set_distribuition(self, distribuition):
		self.distribuition = distribuition


	def set_weight(self, weight):
		self.weight = weight