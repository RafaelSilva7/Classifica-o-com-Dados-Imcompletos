from weka.attribute_selection import ASSearch, ASEvaluation, AttributeSelection

class FeatureSelection():
	"""
	FeatureSelection realiza a seleção de atributo de uma conjunto de dados
	data -> weka.dataset.Instances
	"""
	def __init__(self, data):
		self.original_data = data
		self.featureSelection()

	def featureSelection(self):
		alg_search = ASSearch(classname="weka.attributeSelection.GeneticSearch", options=["-Z", "1024", "-G", "20", "-C", "0.6", "-M", "0.3"])
		alg_evaluation = ASEvaluation(classname="weka.attributeSelection.CfsSubsetEval", options=["-P", "1", "-E", "1"])
		feature_selection = AttributeSelection()
		feature_selection.search(alg_search)
		feature_selection.evaluator(alg_evaluation)
		feature_selection.select_attributes(self.original_data)
		self.selected_features = feature_selection.selected_attributes
		self.num_features = feature_selection.number_attributes_selected
		self.data_selected = feature_selection.reduce_dimensionality(self.original_data)
