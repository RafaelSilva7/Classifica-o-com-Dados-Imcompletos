
class MissingPatterns():

	"""docstring for MissingPatterns"""
	def __init__(self, data):
		self.missing_patterns = set() # Missing Patterns -> set de frozenset
		self.data = data
		self.execute();

	def execute(self):
		for instance in self.data.data:
			temp = set() # Set
			for i,feature in enumerate(instance, start=0):
				if feature is '?':
					temp.add(i)
			self.missing_patterns.add(frozenset(temp)) #set(map(frozenset, t))
			temp.clear()
