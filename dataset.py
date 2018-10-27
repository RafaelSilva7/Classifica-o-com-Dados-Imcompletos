import re

class Dataset():

	def __init__(self, name='hepatitis'):
		self.name = name
		self.data = []
		self.data_class = []
		self.n_instances = None
		self.n_features = None
		self.n_class = None
		#self.n_integer = None
		#self.n_real = None
		#self.n_nominal = None
		self.instance_data()

	"""Instancia a base de dados"""
	def instance_data(self):
		name_file = 'Dataset/'+self.name+'/'+self.name+'.data'
		with open(name_file) as f:
			for instance in f:
				lis = re.findall(r'\d*\.\d+|\d+|\?', instance)
				self.data_class.append(lis[0])
				self.data.append(lis[1::])
			f.close()

			self.n_instances = len(self.data_class)
			self.n_features = len(self.data[0])
			self.n_class = len(set(self.data_class))
