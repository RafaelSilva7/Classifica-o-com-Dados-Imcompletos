
class Training():

	d = None # Dataset
	l = None # Algoritmo de classificação

	c = None # Conjunto de classificadores
	w = None # Peso dos classificadores
	sf = None # Conjunto de features selecionadas

	impD = None # Dados imputados
	cp = None # Features de treinamento

	"""docstring for Training"""
	def __init__(self, d, l):
		self.d = d;
		self.l = l;

	"""Realiza o treinamento da classificação"""
	def train():
		pass
		